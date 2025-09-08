#!/bin/bash

# Get all AWS regions
REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Processing region: $region"

  # Get all security groups except the default one
  SG_IDS=$(aws ec2 describe-security-groups \
    --region $region \
    --query "SecurityGroups[?GroupName!='default'].GroupId" \
    --output text)

  if [ -z "$SG_IDS" ]; then
    echo "  No custom security groups found in $region"
  else
    for sg in $SG_IDS; do
      echo "  Deleting security group $sg in $region"
      aws ec2 delete-security-group --group-id $sg --region $region
    done
  fi
done
