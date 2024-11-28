# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Install libaio1 and build dependencies
RUN apt-get update && apt-get install -y libaio1 build-essential libssl-dev libffi-dev python3-dev && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure config.sh is executable
RUN chmod +x config.sh

# Run the config script
RUN ./config.sh

# Set the environment variable for Oracle Instant Client
ENV LD_LIBRARY_PATH=/app/instantclient_23_6

# Expose the port the application runs on
EXPOSE 5010

# Set the FLASK_APP environment variable
ENV FLASK_APP=src/app.py

# Command to run the application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]