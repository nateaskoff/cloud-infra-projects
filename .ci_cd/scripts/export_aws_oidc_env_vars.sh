#!/bin/bash

# Exit on any error
set -e

# Ensure required environment variables are set
: "${AWS_REGION:?Environment variable AWS_REGION is required}"
: "${TF_VAR_assume_role_name:?Environment variable TF_VAR_assume_role_name is required}"
: "${AWS_SESSION_NAME:?Environment variable AWS_SESSION_NAME is required}"
: "${AWS_WEB_IDENTITY_TOKEN_URL:?Environment variable AWS_WEB_IDENTITY_TOKEN_URL is required}"

# Get the Web Identity Token from GitHub Actions OIDC (it's available automatically)
WEB_IDENTITY_TOKEN=$(curl -sL "$AWS_WEB_IDENTITY_TOKEN_URL/.well-known/openid-configuration" | jq -r .issuer)

# Check if the token is fetched successfully
if [ -z "$WEB_IDENTITY_TOKEN" ]; then
  echo "Error: Web Identity Token could not be retrieved."
  exit 1
fi

# Assume role using AWS CLI and Web Identity Token
CREDS_JSON=$(aws sts assume-role-with-web-identity \
  --role-arn "$TF_VAR_assume_role_name" \
  --role-session-name "$AWS_SESSION_NAME" \
  --web-identity-token "$WEB_IDENTITY_TOKEN" \
  --duration-seconds 3600 \
  --region "$AWS_REGION" \
  --output json)

# Extract the temporary credentials from the assume-role response
AWS_ACCESS_KEY_ID=$(echo $CREDS_JSON | jq -r .Credentials.AccessKeyId)
AWS_SECRET_ACCESS_KEY=$(echo $CREDS_JSON | jq -r .Credentials.SecretAccessKey)
AWS_SESSION_TOKEN=$(echo $CREDS_JSON | jq -r .Credentials.SessionToken)

# Generate the credentials file in /tmp/aws-oidc-credentials
CREDENTIALS_FILE="/tmp/aws-oidc-credentials"

mkdir -p $(dirname "$CREDENTIALS_FILE")  # Create the directory if it doesn't exist

# Write the temporary credentials to the file in AWS CLI credentials format
cat <<EOL > "$CREDENTIALS_FILE"
[default]
aws_access_key_id = $AWS_ACCESS_KEY_ID
aws_secret_access_key = $AWS_SECRET_ACCESS_KEY
aws_session_token = $AWS_SESSION_TOKEN
EOL

echo "AWS credentials have been written to $CREDENTIALS_FILE."

# Optionally, verify by listing S3 buckets (or any other AWS command)
echo "Verifying AWS credentials by listing S3 buckets..."
AWS_SHARED_CREDENTIALS_FILE="$CREDENTIALS_FILE" aws s3 ls
