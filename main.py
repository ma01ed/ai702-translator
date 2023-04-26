from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

from translate import translate

class TranslationRequest(BaseModel):
    input_text: str
    translate_from_to: str
    model: str = "Helsinki-NLP/opus-mt-en-ar"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# For only index.html (no other files)
@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.post("/translate")
async def translate_text(input: TranslationRequest):
    """
    Endpoint to translate text from one language to another using a specified model.
    """
    print(input)
    
    # Translate text using specified model
    translated_text = translate(input.model, input.translate_from_to, input.input_text)
    return {"input_text": input.input_text, "output_text": translated_text, "model": input.model }