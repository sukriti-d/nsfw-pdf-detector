from fastapi import FastAPI, File, UploadFile
from app.nsfw_detector import detect_nsfw_in_pdf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the NSFW PDF Detection API"}

@app.post("/analyze/pdf")
async def analyze_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    result = detect_nsfw_in_pdf(contents)
    return {"nsfw_pages": result}
