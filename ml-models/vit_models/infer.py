import torch
from PIL import Image
from transformers import ViTImageProcessor, ViTForImageClassification
import argparse
import os

# Load pretrained model and processor
model_name = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

def predict_image(image_path):
    if not os.path.exists(image_path):
        print(f"[ERROR] File not found: {image_path}")
        return

    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # Forward pass
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]

    print(f"✅ Predicted label: {predicted_label}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ViT inference on an image.")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    args = parser.parse_args()

    predict_image(args.image_path)
