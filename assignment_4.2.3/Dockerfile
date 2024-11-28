# Stage 1: Build Stage
# Use a base image with Python
FROM python:3.9-slim as build

# Install system dependencies for Python and virtualenv
RUN apt-get update && apt-get install -y python3-venv python3-tk libgtk2.0-dev libgconf-2-4 && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only the files required to install dependencies
COPY setup.py /app/setup.py
COPY src /app/src

# Create a virtual environment in the container
RUN python3 -m venv /app/venv

# Install dependencies via setup.py inside the virtual environment
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install .

# Stage 2: Final Stage
# Use a minimal base image for the final stage
FROM python:3.9-slim as final

# Set working directory for the application
WORKDIR /app

# Install necessary system dependencies for running the app
RUN apt-get update && apt-get install -y libgtk2.0-dev libgconf-2-4 && rm -rf /var/lib/apt/lists/*

# Create a non-root user for running the application
RUN useradd -m appuser
USER appuser

# Copy the virtual environment and application code from the build stage
COPY --from=build /app /app

# Set the PATH to use the virtual environment's Python and pip by default
ENV PATH="/app/venv/bin:$PATH"

# Set the command to run your application
CMD ["python", "src/nonstandardcode.py"]
