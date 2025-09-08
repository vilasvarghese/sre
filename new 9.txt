#!/bin/bash

# Get all AWS regions
REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Processing region: $region"

  # Get all instance IDs in the region
  INSTANCE_IDS=$(aws ec2 describe-instances \
    --region $region \
    --query "Reservations[].Instances[].InstanceId" \
    --output text)

  for id in $INSTANCE_IDS; do
    echo "  Disabling termination protection for $id in $region"
    aws ec2 modify-instance-attribute \
      --instance-id $id \
      --no-disable-api-termination \
      --region $region
  done
done
