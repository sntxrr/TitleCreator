# TitleCreator
Inspired by a salesperson who would always introduce me with a new title on every call

## Maintainer
[Gabe Abinante (gabinante)](https://github.com/gabinante)

## Contributors

* [Don O'Neill (sntxrr)](https://github.com/rrxtns)
* [Joe Block (unixorn)](https://github.com/unixorn)
* [Brandon McNama (DWSR)](https://github.com/DWSR)


## Instructions to get a new title:
https://title-gen.appspot.com

## Instructions to run locally:
Enter this in the command line:

`Python TitleCreator.py` or `./TitleCreator.py` on Linux/BSD/macOS.

^ You did it! You have a new title! Add it to your Linkedin.

## Instructions to run with Docker:

1.  **Build the Docker image:**
    Open your terminal in the root directory of this project (where the `Dockerfile` is located) and run:
    ```bash
    docker build -t titlecreator .
    ```

2.  **Run the Docker container:**
    After the image is built successfully, you can get a new title by running:
    ```bash
    docker run --rm titlecreator
    ```
    The `--rm` flag automatically removes the container when it exits.

## Using the Public Docker Image (from GHCR)

This repository automatically builds and publishes a Docker image to the GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch.

You can pull and run this pre-built image directly:

1.  **Pull the latest image:**
    ```bash
    docker pull ghcr.io/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME:latest
    ```
    *(You'll need to replace `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME` with the actual path to this repository, e.g., `gabinante/TitleCreator` if that's the correct path)*

2.  **Run the container:**
    ```bash
    docker run --rm ghcr.io/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME:latest
    ```

    This will output a new title, just like running it locally or building it yourself.

#### COMING SOON

a `golang` version 