import sys
import torch
from transformers import AutoFeatureExtractor, AutoModel
from PIL import Image

def main():
    if len(sys.argv) != 2:
        print("Usage: python image_embedding.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]

    # Load pre-trained model and feature extractor
    model_name = "google/vit-base-patch16-224"
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Load and preprocess the image
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Compute the image embedding
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the embedding from the last hidden state
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

    # Print the embedding to stdout
    print(embedding)

if __name__ == "__main__":
    main()
