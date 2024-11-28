# Use a base image with Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Python and virtualenv
RUN apt-get update && apt-get install -y python3-venv python3-tk libgtk2.0-dev libgconf-2-4 && rm -rf /var/lib/apt/lists/*

# Copy only the files required to install dependencies
COPY setup.py /app/setup.py
COPY src /app/src

# Create a virtual environment in the container
RUN python3 -m venv /app/venv

# Activate the virtual environment and install dependencies via setup.py
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install .

# Set the PATH to use the virtual environment's Python and pip by default
ENV PATH="/app/venv/bin:$PATH"

# Set the command to run your application
CMD ["python", "src/nonstandardcode.py"]
