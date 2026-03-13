from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel) : 
    text : str

@app.get("/Health")
def health() : 
    return {"status" : "ok boss"}


@app.post("/analyze")
def alayze_text(data : TextRequest) :
    text = data.text
    word_count = len(text.split())
    char_count = len(text)

    return {
        "text" : text,
        "word_count": word_count,
        "char_count" : char_count
    }