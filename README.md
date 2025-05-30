# TitleCreator
Inspired by a salesperson who would always introduce me with a new title on every call

## Maintainer
[Gabe Abinante (gabinante)](https://github.com/gabinante)

## Contributors

* [Don O'Neill (sntxrr)](https://github.com/sntxrr)
* [Joe Block (unixorn)](https://github.com/unixorn)
* [Brandon McNama (DWSR)](https://github.com/DWSR)


## Instructions to get a new title:
https://title-gen.appspot.com

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

## Using the Public Docker Image (from GHCR)

This repository automatically builds and publishes a Docker image to the GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch.

### CLI Mode
```bash
docker run --rm ghcr.io/sntxrr/TitleCreator:latest
```

### Web UI Mode
```bash
docker run --rm -p 8080:8080 -e WEB_MODE=true ghcr.io/sntxrr/TitleCreator:latest
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

1. **Install the Google Cloud SDK** if you haven't already.

2. **Authenticate with Google Cloud:**
   ```bash
   gcloud auth login
   ```

3. **Set your project ID:**
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```

4. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy titlecreator \
     --image ghcr.io/sntxrr/titlecreator:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars WEB_MODE=true
   ```

   Replace `us-central1` with your preferred region.

5. **Access your service:**
   After deployment, Cloud Run will provide you with a URL where your service is accessible.
   You can access the JSON API using:
   ```bash
   # Using the dedicated endpoint
   curl https://your-service-url/api/title
   
   # Or using the Accept header
   curl -H "Accept: application/json" https://your-service-url/
   ```


## Using the Public Docker Image (from GHCR)

This repository automatically builds and publishes a Docker image to the GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch.

You can pull and run this pre-built image directly:

1.  **Pull the latest image:**
    ```bash
    docker pull ghcr.io/sntxrr/titlecreator:latest
    ```


2.  **Run the container:**
    ```bash
    docker run --rm ghcr.io/sntxrr/titlecreator:latest
    ```

    This will output a new title, just like running it locally or building it yourself.


#### COMING SOON

a `golang` version 
