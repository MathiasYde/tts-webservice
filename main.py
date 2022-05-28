from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from typing import Union
import pyttsx3
import uuid
import os

tts = pyttsx3.init()
cache_directory = "cache"

# create cache directory if it doesn't exist
if not os.path.exists(cache_directory):
		os.mkdir(cache_directory)

app = FastAPI()
@app.get("/status")
def read_status():
	return {"status": "ok"}

@app.get("/tts")
async def synthesize_tts(voice: str, text: str):
	filename = f"{uuid.uuid1()}.wav"
	filepath = os.path.join(cache_directory, filename)

	tts.save_to_file(text, filepath)
	tts.runAndWait()

	return FileResponse(filepath)