# TitleCreator
Inspired by a salesperson who would always introduce me with a new title on every call

## Maintainer
[Gabe Abinante (gabinante)](https://github.com/gabinante)

## Contributors

* [Don O'Neill (sntxrr)](https://github.com/sntxrr)
* [Joe Block (unixorn)](https://github.com/unixorn)
* [Brandon McNama (DWSR)](https://github.com/DWSR)


## Instructions to get a new title:
[https://title.sntxrr.codes/](https://title.sntxrr.codes/)

## Instructions to run locally:
Enter this in the command line:

`Python TitleCreator.py` or `./TitleCreator.py` on Linux/BSD/macOS.

^ You did it! You have a new title! Add it to your Linkedin.

## Building and Running with Docker

### Building the Image
First, build the Docker image with the tag `titlecreator:latest`:

```bash
docker build -t titlecreator:latest .
```

### Running Options

#### 1. CLI Mode (Default)
Run the container in CLI mode to get a single title printed to the console:

```bash
docker run --rm titlecreator:latest
```

#### 2. Web UI Mode
Run the container with the web interface, accessible at http://localhost:8080:

```bash
docker run --rm -p 8080:8080 -e WEB_MODE=true titlecreator:latest
```

Then open your browser and visit `http://localhost:8080` to see the interactive web interface with a "Generate Another Title" button.

#### 3. JSON API Mode
The web service provides two ways to get JSON responses:

1. Using the dedicated API endpoint:
```bash
curl http://localhost:8080/api/title
```

2. Using the Accept header:
```bash
curl -H "Accept: application/json" http://localhost:8080/
```

Both will return a JSON response like:
```json
{
    "title": "AI Whisperer of Neural Networks",
    "message": "Congratulations! Your new title is:"
}
```

## Using Pre-built Docker Images

This repository automatically builds and publishes Docker images to both GitHub Container Registry (GHCR) and Google Artifact Registry whenever changes are pushed to the `main` branch.

### Available Images
- **GitHub Container Registry**: `ghcr.io/sntxrr/titlecreator:latest`
- **Google Artifact Registry**: `us-west2-docker.pkg.dev/title-gen/titlegenerator/titlecreator:latest`

### CLI Mode
```bash
# Using GHCR
docker run --rm ghcr.io/sntxrr/titlecreator:latest

# Using Google Artifact Registry (requires authentication)
docker run --rm us-west2-docker.pkg.dev/title-gen/titlegenerator/titlecreator:latest
```

### Web UI Mode
```bash
# Using GHCR
docker run --rm -p 8080:8080 -e WEB_MODE=true ghcr.io/sntxrr/titlecreator:latest

# Using Google Artifact Registry (requires authentication)
docker run --rm -p 8080:8080 -e WEB_MODE=true us-west2-docker.pkg.dev/title-gen/titlegenerator/titlecreator:latest
```

### JSON API Mode
Once the container is running, you can access the JSON API using either:

```bash
# Using the dedicated endpoint
curl http://localhost:8080/api/title

# Or using the Accept header
curl -H "Accept: application/json" http://localhost:8080/
```

## Deploying to Google Cloud Run

### Prerequisites
1. **Install the Google Cloud SDK** if you haven't already.
2. **Authenticate with Google Cloud:**
   ```bash
   gcloud auth login
   ```

### Setup Artifact Registry (First Time Only)
If you're setting up your own instance, you can use the provided setup script:

```bash
PROJECT_ID=your-project-id ./setup-artifact-registry.sh
```

**Note:** If you see "ALREADY_EXISTS: the repository already exists", that's perfectly fine! It means the Artifact Registry is already configured and ready to use.

### Deploy to Cloud Run

#### Option 1: Using gcloud CLI
```bash
gcloud run deploy titlecreator \
  --image us-west2-docker.pkg.dev/title-gen/titlegenerator/titlecreator:latest \
  --platform managed \
  --region us-west1 \
  --allow-unauthenticated \
  --set-env-vars WEB_MODE=true \
  --project title-gen
```

#### Option 2: Using Cloud Run YAML configuration
```bash
gcloud run services replace cloudrun.yaml --region=us-west1 --project title-gen
```

### Access Your Service
After deployment, Cloud Run will provide you with a URL where your service is accessible.

#### Web Interface
Visit the provided URL in your browser to see the beautiful UI with the "Generate Another Title" button.

#### JSON API
You can access the JSON API using:
```bash
# Using the dedicated endpoint
curl https://your-service-url/api/title

# Or using the Accept header
curl -H "Accept: application/json" https://your-service-url/
```

Both will return a JSON response like:
```json
{
    "title": "Supreme AI Whisperer of Neural Networks",
    "message": "Congratulations! Your new title is:"
}
```


## Development

### Running Tests
```bash
python test_titlecreator.py
```

### Local Development
```bash
# CLI mode
python TitleCreator.py

# Web mode
WEB_MODE=true python TitleCreator.py
```


#### COMING SOON

a `golang` version 
