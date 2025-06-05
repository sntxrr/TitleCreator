#!/bin/bash

# Setup script for Google Artifact Registry
# This script helps configure the Artifact Registry repository for TitleCreator

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Setting up Google Artifact Registry for TitleCreator${NC}"

# Check if PROJECT_ID is set
if [ -z "$PROJECT_ID" ]; then
    echo -e "${YELLOW}⚠️  PROJECT_ID environment variable is not set.${NC}"
    echo "Please set it with: export PROJECT_ID=your-gcp-project-id"
    echo "Or run this script with: PROJECT_ID=your-project-id ./setup-artifact-registry.sh"
    exit 1
fi

echo -e "${GREEN}📋 Using Project ID: $PROJECT_ID${NC}"

# Set the region (you can change this if needed)
REGION="us-west2"
REPOSITORY_NAME="titlegenerator"

echo -e "${GREEN}🌍 Using Region: $REGION${NC}"
echo -e "${GREEN}📦 Repository Name: $REPOSITORY_NAME${NC}"

# Enable required APIs
echo -e "${GREEN}🔧 Enabling required APIs...${NC}"
gcloud services enable artifactregistry.googleapis.com --project=$PROJECT_ID
gcloud services enable cloudbuild.googleapis.com --project=$PROJECT_ID
gcloud services enable run.googleapis.com --project=$PROJECT_ID

# Create the Artifact Registry repository
echo -e "${GREEN}📦 Creating Artifact Registry repository...${NC}"
if gcloud artifacts repositories create $REPOSITORY_NAME \
    --repository-format=docker \
    --location=$REGION \
    --description="Docker repository for TitleCreator" \
    --project=$PROJECT_ID 2>/dev/null; then
    echo -e "${GREEN}✅ Repository created successfully!${NC}"
else
    echo -e "${YELLOW}ℹ️  Repository already exists - continuing with setup...${NC}"
fi

# Configure Docker authentication
echo -e "${GREEN}🔑 Configuring Docker authentication...${NC}"
gcloud auth configure-docker $REGION-docker.pkg.dev --quiet

# Create service account for GitHub Actions
echo -e "${GREEN}👤 Creating service account for GitHub Actions...${NC}"
SERVICE_ACCOUNT_NAME="github-actions"
SERVICE_ACCOUNT_EMAIL="$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com"

if gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME \
    --display-name="GitHub Actions Service Account" \
    --description="Service account for GitHub Actions to push to Artifact Registry" \
    --project=$PROJECT_ID 2>/dev/null; then
    echo -e "${GREEN}✅ Service account created successfully!${NC}"
else
    echo -e "${YELLOW}ℹ️  Service account already exists - continuing...${NC}"
fi

# Grant necessary permissions
echo -e "${GREEN}🔐 Granting required permissions...${NC}"
echo "  - Artifact Registry Writer"
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
    --role="roles/artifactregistry.writer" \
    --quiet

echo "  - Cloud Run Admin"
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
    --role="roles/run.admin" \
    --quiet

echo "  - Service Account User (for Cloud Run)"
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
    --role="roles/iam.serviceAccountUser" \
    --quiet

# Create service account key if it doesn't exist
KEY_FILE="github-actions-key.json"
if [ ! -f "$KEY_FILE" ]; then
    echo -e "${GREEN}🔑 Creating service account key...${NC}"
    gcloud iam service-accounts keys create $KEY_FILE \
        --iam-account=$SERVICE_ACCOUNT_EMAIL \
        --project=$PROJECT_ID
    echo -e "${GREEN}✅ Service account key created: $KEY_FILE${NC}"
else
    echo -e "${YELLOW}ℹ️  Service account key already exists: $KEY_FILE${NC}"
fi

echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo -e "${YELLOW}📝 Remaining manual steps:${NC}"
echo "1. Add the following secrets to your GitHub repository:"
echo "   - GCP_SA_KEY: Contents of $KEY_FILE"
echo "   - GCP_PROJECT_ID: $PROJECT_ID"
echo ""
echo "2. To add secrets to GitHub repository, run:"
echo "   gh secret set GCP_SA_KEY < $KEY_FILE"
echo "   gh secret set GCP_PROJECT_ID --body \"$PROJECT_ID\""
echo "   (requires GitHub CLI: https://cli.github.com/)"
echo ""
echo -e "${GREEN}🚀 What happens next:${NC}"
echo "• Push to main branch → Automatic build & push to Artifact Registry"
echo "• New image → Automatic deployment to Cloud Run"
echo "• Your app will be automatically updated with each code change!"
echo ""
echo -e "${GREEN}🎉 Your Artifact Registry is ready at:${NC}"
echo "   $REGION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/titlecreator"