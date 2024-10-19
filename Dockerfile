# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Expose any necessary ports (if applicable)
EXPOSE 8080

# Define environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the executable when the container starts
ENTRYPOINT ["python", "main.py"]
