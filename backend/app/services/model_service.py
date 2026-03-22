import torch
import torchvision.models as models
import torch.nn as nn
from torchvision import transforms
from PIL import Image

class ModelService:
    def __init__(self, model_path):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # 🔥 Recreate architecture
        self.model = models.efficientnet_b0(pretrained=False)

        self.model.classifier = nn.Sequential(
            nn.Dropout(0.4),
            nn.Linear(self.model.classifier[1].in_features, 2)
        )

        # 🔥 Load weights
        self.model.load_state_dict(
            torch.load(model_path, map_location=self.device)
        )

        self.model.to(self.device)
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

    def predict(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(image)
            probs = torch.softmax(outputs, dim=1)
            conf, pred = torch.max(probs, 1)

        label = "PNEUMONIA" if pred.item() == 1 else "NORMAL"

        return {
            "prediction": label,
            "confidence": float(conf.item())
        }