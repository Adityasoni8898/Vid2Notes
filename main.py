import requests
import Functions.Transcription, Functions.NotesMaker, Functions.Youtube_to_mp3, Functions.ImageScrapper, Functions.QuizGenerator
from fastapi import FastAPI
from fastapi.params import Body
import json
from fastapi.params import Body
import uvicorn
from fastapi.params import Body
import json

app = FastAPI()


@app.post("/vid2notes/notes_generator")
def vid2notes(payload : dict = Body(...)):
    
    api_key = ""
    gemini_key = ""
    ytlink = payload["url"]

    title = Functions.Youtube_to_mp3.youtube_mp3(ytlink)
    video_path = title
    video_file = open(video_path, "rb")

    transcript = Functions.Transcription.whisper(api_key, video_file)
    cleanNotes = Functions.NotesMaker.gemini(gemini_key, transcript)
    print(cleanNotes)
    
    cleanNotes = json.loads(cleanNotes)

    return cleanNotes


@app.post("/vid2notes/image_scrapper")
def image_scrapper(payload : dict = Body(...)):
    image_url = Functions.ImageScrapper.image_scrapper(payload["keyword"])
    return {"image_url" : image_url}


@app.post("/vid2notes/quiz_generator")
def quiz_generator(payload : dict = Body(...)):
    quiz = Functions.QuizGenerator.quiz_generator("AIzaSyAledNIKjVN1-yY3qHWTgZkNDeZYdI14pc", payload["title"], payload["content"])
    print(quiz)
    quiz_json = json.loads(quiz)
    
    return quiz_json


if __name__ == "__main__" :
    app.run(debug=True)