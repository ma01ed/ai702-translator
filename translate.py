from transformers import pipeline

# Translate text using HuggingFace pipeline
def translate(model_name, lang_pair, text):
    translator = pipeline(lang_pair, model=model_name)
    result = translator(text)
    return result[0]['translation_text']