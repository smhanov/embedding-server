# Image Embedding Service

This project provides a simple HTTP server that generates embeddings for images using a pre-trained Vision Transformer (ViT) model.

## Prerequisites

- Docker
- NVIDIA GPU (optional, but recommended for better performance)

## Getting Started

### Setting up Docker with NVIDIA CUDA support

If you have an NVIDIA GPU and want to use it for faster processing, you need to set up Docker to work with NVIDIA CUDA drivers:

1. Install the NVIDIA driver for your GPU if you haven't already.
2. Install the NVIDIA Container Toolkit:
   - For Ubuntu: Follow the instructions at [NVIDIA Container Toolkit Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)
   - For other operating systems, refer to the appropriate guide in the NVIDIA documentation.

3. Verify the installation:
   ```
   sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
   ```
   If successful, this command should display information about your GPU.

### Running the Image Embedding Service

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build the Docker image:
   ```
   docker build -t image-embedding-service .
   ```

3. Run the Docker container:
   - Without GPU:
     ```
     docker run -p 8080:8080 image-embedding-service
     ```
   - With GPU (if NVIDIA Container Toolkit is set up):
     ```
     docker run --gpus all -p 8080:8080 image-embedding-service
     ```

   The server will start and listen on `http://localhost:8080`.

## Usage

To get an embedding for an image, send a POST request to the server with the image file. Here's an example using curl:

```
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:8080
```

Replace `/path/to/your/image.jpg` with the actual path to the image file you want to process.

The server will respond with a JSON array representing the image embedding.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [NVIDIA Container Toolkit Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html)
- [PyTorch with GPU Support](https://pytorch.org/get-started/locally/)
