from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random

app = FastAPI()

class Question(BaseModel):
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/api/ask")
async def ask_question(question: Question):
    responses = [
        "It is certain", "It is decidedly so", "Without a doubt",
        "Yes definitely", "You may rely on it", "As I see it, yes",
        "Most likely", "Outlook good", "Yes", "Signs point to yes",
        "Reply hazy, try again", "Ask again later",
        "Better not tell you now", "Cannot predict now",
        "Concentrate and ask again", "Don't count on it", 
        "My reply is no", "My sources say no",
        "Outlook not so good", "Very doubtful"
    ]
    return {"answer": random.choice(responses)}
