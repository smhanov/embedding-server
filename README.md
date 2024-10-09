# Image Embedding Service

This project provides a simple HTTP server that generates embeddings for images using a pre-trained Vision Transformer (ViT) model.

## Prerequisites

- Docker

## Getting Started

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
   ```
   docker run -p 8080:8080 image-embedding-service
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
