from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/", StaticFiles(directory="static", html=True), name="static")

RESPONSES = {
    "affirmative": [
        "It is certain",
        "It is decidedly so", 
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes"
    ],
    "non_committal": [
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again"
    ],
    "negative": [
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good", 
        "Very doubtful"
    ]
}

@app.post("/api/ask")
async def ask_question(question: dict):
    all_responses = RESPONSES["affirmative"] + RESPONSES["non_committal"] + RESPONSES["negative"]
    return {"answer": random.choice(all_responses)}
