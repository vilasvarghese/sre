#!/bin/bash

# Get all AWS regions
REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Processing region: $region"

  # Get all instance IDs in this region
  INSTANCE_IDS=$(aws ec2 describe-instances \
    --region $region \
    --query "Reservations[].Instances[].InstanceId" \
    --output text)

  if [ -z "$INSTANCE_IDS" ]; then
    echo "  No instances found in $region"
  else
    for id in $INSTANCE_IDS; do
      echo "  Terminating instance $id in $region"
      aws ec2 terminate-instances --instance-ids $id --region $region
    done
  fi
done
