#!/bin/bash

# Get all AWS regions
REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Processing region: $region"

  # Get all non-default VPCs in this region
  VPC_IDS=$(aws ec2 describe-vpcs \
    --region $region \
    --query "Vpcs[?IsDefault==\`false\`].VpcId" \
    --output text)

  if [ -z "$VPC_IDS" ]; then
    echo "  No non-default VPCs found in $region"
  else
    for vpc in $VPC_IDS; do
      echo "  Processing VPC: $vpc"

      # --- Step 1: Detach and delete Internet Gateways ---
      IGW_IDS=$(aws ec2 describe-internet-gateways \
        --region $region \
        --filters "Name=attachment.vpc-id,Values=$vpc" \
        --query "InternetGateways[].InternetGatewayId" \
        --output text)

      for igw in $IGW_IDS; do
        echo "    Detaching and deleting IGW: $igw"
        aws ec2 detach-internet-gateway --internet-gateway-id $igw --vpc-id $vpc --region $region
        aws ec2 delete-internet-gateway --internet-gateway-id $igw --region $region
      done

      # --- Step 2: Delete subnets ---
      SUBNET_IDS=$(aws ec2 describe-subnets \
        --region $region \
        --filters "Name=vpc-id,Values=$vpc" \
        --query "Subnets[].SubnetId" \
        --output text)

      for subnet in $SUBNET_IDS; do
        echo "    Deleting Subnet: $subnet"
        aws ec2 delete-s
