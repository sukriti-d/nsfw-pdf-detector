import nsfwlib
from PIL import Image
import numpy as np

# Load model once globally
model = nsfwlib.load_model()

def load_model_and_predict(image: Image.Image):
    image = image.resize((224, 224))
    prediction = nsfwlib.predict(image, model)
    
    # You can adjust based on the actual keys provided by your model
    nsfw_score = prediction.get("porn", 0) + prediction.get("sexy", 0)
    
    return {
        "nsfw_score": nsfw_score,
        "full_prediction": prediction
    }
