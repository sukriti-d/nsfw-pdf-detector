import fitz  # PyMuPDF
from PIL import Image
import io
import numpy as np
from app.utils import load_model_and_predict

def detect_nsfw_in_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    nsfw_pages = []

    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        
        # Predict NSFW score
        prediction = load_model_and_predict(image)
        if prediction.get("nsfw_score", 0) > 0.6:
            nsfw_pages.append(i + 1)

    return nsfw_pages
