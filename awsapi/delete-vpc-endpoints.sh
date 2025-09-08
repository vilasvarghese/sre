#!/bin/bash

# Get all AWS regions
REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Processing region: $region"

  # Get all VPC Endpoint IDs in this region
  VPCE_IDS=$(aws ec2 describe-vpc-endpoints \
    --region $region \
    --query "VpcEndpoints[].VpcEndpointId" \
    --output text)

  if [ -z "$VPCE_IDS" ]; then
    echo "  No VPC Endpoints found in $region"
  else
    for vpce in $VPCE_IDS; do
      echo "  Deleting VPC Endpoint $vpce in $region"
      aws ec2 delete-vpc-endpoints --vpc-endpoint-ids $vpce --region $region
    done
  fi
done
