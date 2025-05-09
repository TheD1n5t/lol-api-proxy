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

    print(">> Request to:", url)
    print(">> Status code:", response.status_code)
    print(">> Response text:", response.text)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json()
