# Use a smaller base image (Debian Slim)
FROM python:3.8-slim AS builder

# Set the working directory
WORKDIR /workdir

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the script into the container
COPY script.py .

# Define a volume for input/output files
VOLUME ["/workdir"]

# Set the entrypoint to run the script
ENTRYPOINT ["python", "/workdir/script.py"]
