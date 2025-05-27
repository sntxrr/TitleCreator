# Use an official Python 3 slim base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY TitleCreator.py .

# Make the script executable (though it's run with python interpreter)
# RUN chmod +x TitleCreator.py

# Set the command to run when the container starts
CMD ["python", "./TitleCreator.py"]
