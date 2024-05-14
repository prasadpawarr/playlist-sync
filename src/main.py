from fastapi import FastAPI
from .routers import playlists

app = FastAPI()

app.include_router(playlists.router)


@app.get("/")
async def home():
    return {"message": "Hola Amigo!"}
