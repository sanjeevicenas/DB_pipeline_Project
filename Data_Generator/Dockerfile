# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY . .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose necessary ports (if needed, e.g., Kafka communication)
# Optional: Expose port if required for external communication.
# EXPOSE 9092

# Step 6: Define the default command to run your script
CMD ["python", "./E_commerce_data_generator.py"]