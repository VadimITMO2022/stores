# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./app /app

# Command to run the application with Gunicorn
# Binds Gunicorn to port 8000, accessible within the Docker network
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dashboard:app"]
