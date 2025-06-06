#!/bin/bash

set -e

echo "🚀 Setting up TitleCreator development environment..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Install Google Cloud CLI
echo "☁️ Installing Google Cloud CLI..."
if ! command -v gcloud &> /dev/null; then
    echo "Installing gcloud CLI..."
    # Download and install gcloud CLI
    curl -sSL https://sdk.cloud.google.com | bash
    
    # Add gcloud to PATH for current session
    export PATH="$HOME/google-cloud-sdk/bin:$PATH"
    
    # Add to bashrc for future sessions
    echo 'export PATH="$HOME/google-cloud-sdk/bin:$PATH"' >> ~/.bashrc
    
    echo "✅ Google Cloud CLI installed"
else
    echo "✅ Google Cloud CLI already installed"
fi

# Make scripts executable
echo "🔧 Setting up scripts..."
chmod +x setup-artifact-registry.sh

# Create helpful aliases
echo "🔗 Setting up development aliases..."
cat << 'EOF' >> ~/.bashrc

# TitleCreator development aliases
alias tc-cli='python TitleCreator.py'
alias tc-web='WEB_MODE=true python TitleCreator.py'
alias tc-test='python test_titlecreator.py'
alias tc-build='docker build -t titlecreator:local .'
alias tc-run='docker run --rm titlecreator:local'
alias tc-web-docker='docker run --rm -p 8080:8080 -e WEB_MODE=true titlecreator:local'

EOF

echo "✅ Development environment setup complete!"
echo ""
echo "🎉 You can now:"
echo "  • Run 'tc-cli' for CLI mode"
echo "  • Run 'tc-web' for web mode"
echo "  • Run 'tc-test' to run tests"
echo "  • Run 'tc-build' to build Docker image"
echo ""
echo "🔧 For Google Cloud setup:"
echo "  • Run 'gcloud auth login' to authenticate"
echo "  • Run 'PROJECT_ID=your-project ./setup-artifact-registry.sh'" 