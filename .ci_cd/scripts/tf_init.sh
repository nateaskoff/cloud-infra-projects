#!/bin/bash

if terraform init -input=false; then
    echo "Terraform init successful";
else
    echo "Creating workspace";
    terraform workspace new $TF_WORKSPACE;
    terraform init -input=false;
fi
