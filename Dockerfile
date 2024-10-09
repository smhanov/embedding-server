# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir torch transformers pillow numpy

# Pre-download the model
RUN python -c "from transformers import AutoFeatureExtractor, AutoModel; model_name='google/vit-base-patch16-224'; AutoFeatureExtractor.from_pretrained(model_name); AutoModel.from_pretrained(model_name)"

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run image_embedding.py when the container launches
CMD ["python", "image_embedding.py"]
