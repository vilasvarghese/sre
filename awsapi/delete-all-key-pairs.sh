#!/bin/bash

# Get all AWS regions
REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Processing region: $region"

  # Get all key pairs in the region
  KEY_NAMES=$(aws ec2 describe-key-pairs \
    --region $region \
    --query "KeyPairs[].KeyName" \
    --output text)

  if [ -z "$KEY_NAMES" ]; then
    echo "  No key pairs found in $region"
  else
    for key in $KEY_NAMES; do
      echo "  Deleting key pair: $key in $region"
      aws ec2 delete-key-pair --key-name "$key" --region $region
    done
  fi
done
