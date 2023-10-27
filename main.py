import Functions.Transcription, Functions.NotesMaker, Functions.youtube_to_mp3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/vid2notes", methods=["POST"])
def vid2notes():
    api_key = <api key>
    data = request.get_json()
    ytlink = data["url"]

    title = Functions.youtube_to_mp3.youtube_mp3(ytlink)
    video_path = title
    video_file = open(video_path, "rb")

    transcript = Functions.Transcription.whisper(api_key, video_file)
    cleanNotes = Functions.NotesMaker.gpt(api_key, transcript)

    notes = {
        "notes" : cleanNotes,
        "video_title" : title
    } 

    return notes, 201

if __name__ == "__main__" :
    app.run(debug=True)





