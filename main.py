from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from chat import get_completion_from_messages,collect_messages_text

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    content: str

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: Message):
    user_message = message.content
    response = collect_messages_text(user_message)

    return {"message": response}

@app.post("/process_voice")
async def process_voice(voice_input: dict):
    # print(voice_input)
    text = voice_input.get('input')
    # Process the voice input as needed
    # print("Voice input:", text)
    response = collect_messages_text(text)
    # print(response)
    return {"message": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
