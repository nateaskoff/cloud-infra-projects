import sys
import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Script input
cloud_providers_input = sys.argv[1]

def setup_ci_cd(cloud_providers):
    '''Drops the correct credentials file for each cloud provider and sets up the CI/CD pipeline.'''
    # Use a set to remove duplicates and then convert it back to a list
    unique_providers = list(set(provider.strip() for provider in cloud_providers))

    for provider in unique_providers:
        if provider == 'Az':
            # Azure setup
            az_env_vars = os.getenv('AZURE_CREDENTIALS')
            azure_org = os.getenv('AZURE_ORG')
            azure_project = os.getenv('AZURE_PROJECT')
            if not az_env_vars:
                logger.error('No Azure credentials found. Exiting...')
                sys.exit(1)

            # Write Azure credentials to file
            with open('az_credentials.json', 'w') as f:
                f.write(az_env_vars)

            # Set up Azure CI/CD pipeline
            subprocess.run(['az', 'devops', 'configure', '--defaults',
                            f'organization=https://dev.azure.com/{azure_org}/',
                            f'project={azure_project}'])

        elif provider == 'Gc':
            # Google Cloud setup
            gc_env_vars = os.getenv('GOOGLE_CREDENTIALS')
            gcp_project = os.getenv('GCP_PROJECT')
            gcp_zone = os.getenv('GCP_ZONE')
            if not gc_env_vars:
                logger.error('No Google credentials found. Exiting...')
                sys.exit(1)

            # Write Google Cloud credentials to file
            with open('gc_credentials.json', 'w') as f:
                f.write(gc_env_vars)

            # Set up Google Cloud CI/CD pipeline
            subprocess.run(['gcloud', 'config', 'set', 'project', gcp_project])
            subprocess.run(['gcloud', 'config', 'set', 'compute/zone', gcp_zone])

        elif provider == 'Aw':
            # AWS setup
            aw_env_vars = os.getenv('AWS_CREDENTIALS')
            aws_region = os.getenv('AWS_REGION')
            aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

            if not aw_env_vars:
                logger.error('No AWS credentials found. Exiting...')
                sys.exit(1)

            # Write AWS credentials to file
            with open('aw_credentials.json', 'w') as f:
                f.write(aw_env_vars)

            # Set up AWS CI/CD pipeline
            subprocess.run(['aws', 'configure', 'set', 'region', aws_region])
            subprocess.run(['aws', 'configure', 'set', 'aws_access_key_id', aws_access_key_id])
            subprocess.run(['aws', 'configure', 'set', 'aws_secret_access_key', aws_secret_access_key])

        else:
            logger.warning(f'Unknown cloud provider: {provider}')

    logger.info('CI/CD pipeline setup complete.')

if __name__ == '__main__':
    # Split the input on commas, remove duplicates, and strip whitespace
    cloud_providers = cloud_providers_input.split(',')
    setup_ci_cd(cloud_providers)
