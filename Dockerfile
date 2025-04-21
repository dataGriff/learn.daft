# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for Azure Data Lake connection
ENV AZURE_STORAGE_ACCOUNT_NAME=<your_account_name>
ENV AZURE_STORAGE_ACCOUNT_KEY=<your_account_key>

# Run the Python application
CMD ["python", "app.py"]