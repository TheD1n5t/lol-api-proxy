from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Erlaube CORS für dein GitHub Pages Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Du kannst das später einschränken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RIOT_API_KEY = os.getenv("RIOT_API_KEY")  # Sicher aus Umgebungsvariablen

@app.get("/summoner/{summoner_name}")
def get_summoner_data(summoner_name: str):
    url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()
