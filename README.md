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

## Instructions to run with Docker:

### CLI Mode (Default)
By default, the container runs in CLI mode and outputs a title directly:

1.  **Build the Docker image:**
    Open your terminal in the root directory of this project (where the `Dockerfile` is located) and run:
    ```bash
    docker build -t titlecreator .
    ```

2.  **Run the Docker container in CLI mode:**
    ```bash
    docker run --rm titlecreator
    ```
    The `--rm` flag automatically removes the container when it exits.

### Web Service Mode
To run the container as a web service:

```bash
docker run --rm -p 8080:8080 -e WEB_MODE=true titlecreator
```

Then access the service at `http://localhost:8080` to get a JSON response with your title.

## Using the Public Docker Image (from GHCR)

This repository automatically builds and publishes a Docker image to the GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch.

### CLI Mode
```bash
docker run --rm ghcr.io/sntxrr/TitleCreator:latest
```

### Web Service Mode
```bash
docker run --rm -p 8080:8080 -e WEB_MODE=true ghcr.io/sntxrr/TitleCreator:latest
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
     --image ghcr.io/sntxrr/TitleCreator:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars WEB_MODE=true
   ```

   Replace `us-central1` with your preferred region.

5. **Access your service:**
   After deployment, Cloud Run will provide you with a URL where your service is accessible.

#### COMING SOON

a `golang` version 