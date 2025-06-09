# GitHub Codespaces Setup for TitleCreator

This repository is configured with a pre-built GitHub Codespaces environment that includes all the tools you need to develop, test, and deploy TitleCreator.

## 🚀 Quick Start

1. **Open in Codespaces**:
   - Click the `<> Code` button on the GitHub repository
   - Select `Create codespace on main`
   - Wait for the environment to build (first time takes ~3-5 minutes)

2. **Environment will include**:
   - ✅ Python 3.12 with Flask and dependencies
   - ✅ Docker and Docker Compose
   - ✅ Google Cloud CLI (`gcloud`)
   - ✅ GitHub CLI (`gh`)
   - ✅ VS Code extensions for Python, Docker, YAML
   - ✅ Port 8080 automatically forwarded for the web app

## 🛠️ What's Pre-configured

### Development Tools
- **Python**: Version 3.9 with pip
- **Docker**: Docker-in-Docker for building and testing containers
- **gcloud CLI**: For Google Cloud operations
- **GitHub CLI**: For repository management

### VS Code Extensions
- Python support with linting and formatting
- Docker extension for container management
- YAML support for configuration files
- GitHub Copilot (if you have access)

### Port Forwarding
- Port 8080 is automatically forwarded and labeled as "TitleCreator Web App"
- Opens in preview mode when the app starts

## 📝 Development Workflow

### 1. Test the Application Locally
```bash
# CLI mode
python TitleCreator.py

# Web mode  
WEB_MODE=true python TitleCreator.py
```

### 2. Build and Test Docker Container
```bash
# Build the image
docker build -t titlecreator:local .

# Test CLI mode
docker run --rm titlecreator:local

# Test web mode
docker run --rm -p 8080:8080 -e WEB_MODE=true titlecreator:local
```

### 3. Run Tests
```bash
python test_titlecreator.py
```

### 4. Google Cloud Setup (Optional)
If you want to test deployment:
```bash
# Authenticate with Google Cloud
gcloud auth login

# Run the setup script
PROJECT_ID=your-project-id ./setup-artifact-registry.sh
```

## 🔧 Customizing the Environment

### Adding Dependencies
1. Update `requirements.txt`
2. Rebuild the Codespace or run: `pip install -r requirements.txt`

### Adding VS Code Extensions
Edit `.devcontainer/devcontainer.json` and add extensions to the `extensions` array:
```json
"extensions": [
    "existing.extension",
    "new.extension-id"
]
```

### Environment Variables
Add environment variables in `.devcontainer/devcontainer.json`:
```json
"containerEnv": {
    "YOUR_VAR": "value"
}
```

## 🚀 Setting Up Prebuilds (Repository Admin)

To speed up Codespace creation for all contributors:

1. **Go to Repository Settings** → **Codespaces**
2. **Set up prebuilds**:
   - Configuration: `.devcontainer/devcontainer.json`
   - Region: Choose closest to your team
   - Trigger: On push to main branch
   - Template selection: Use the devcontainer configuration

3. **Prebuild triggers**:
   - When `.devcontainer/` files change
   - When `requirements.txt` changes
   - When `Dockerfile` changes

## 💡 Tips

### Quick Commands
- **Start web app**: `WEB_MODE=true python TitleCreator.py`
- **Run tests**: `python test_titlecreator.py`
- **Build Docker**: `docker build -t titlecreator .`
- **Format code**: `black TitleCreator.py`

### Accessing Your App
- When running in web mode, click the "Open in Browser" button that appears
- Or use the "Ports" tab to access port 8080

### GitHub Integration
- The GitHub CLI (`gh`) is pre-authenticated
- You can manage PRs, issues, and secrets directly from the terminal

## 🐛 Troubleshooting

### Codespace Won't Start
- Check `.devcontainer/devcontainer.json` syntax
- Look at the creation logs in the Codespaces tab

### Dependencies Missing
- Rebuild the container: `Ctrl+Shift+P` → "Codespaces: Rebuild Container"
- Or manually install: `pip install -r requirements.txt`

### Port Not Forwarding
- Check the "Ports" tab in VS Code
- Manually forward port 8080 if needed

## 📚 Resources

- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [Dev Container Reference](https://containers.dev/implementors/json_reference/)
- [VS Code Codespaces](https://code.visualstudio.com/docs/remote/codespaces) 