# Use an official Python 3 slim base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY titlecreator.py .

# Make the script executable
RUN chmod +x titlecreator.py

# Expose the port the app runs on (only used in web mode)
EXPOSE 8080

# Set environment variable for web mode (can be overridden at runtime)
ENV WEB_MODE=false

# Set the command to run when the container starts
CMD ["python", "titlecreator.py"]
