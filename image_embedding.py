import torch
from transformers import AutoFeatureExtractor, AutoModel
from PIL import Image
import numpy as np
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

# Load pre-trained model and feature extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def extract_features(image_file):
    # Load and preprocess the image
    image = Image.open(image_file)
    image = image.convert("RGB")
    image = np.array(image)
    inputs = feature_extractor(images=[image], return_tensors="pt")

    # Compute the image embedding
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the embedding from the last hidden state
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embedding.tolist()

class ImageEmbeddingHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_type, _ = cgi.parse_header(self.headers['Content-Type'])
        if content_type != 'multipart/form-data':
            self.send_error(400, "Bad request: must be multipart/form-data")
            return

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        if 'file' not in form:
            self.send_error(400, "Bad request: missing file parameter")
            return

        file_item = form['file']
        if not file_item.file:
            self.send_error(400, "Bad request: file is empty")
            return

        try:
            embedding = extract_features(file_item.file)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(embedding).encode())
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")

def main():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, ImageEmbeddingHandler)
    print("Server running on port 8080")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
