import Functions.Transcription, Functions.NotesMaker

api_key = "<your key>"

video_path = "Assets/How To Use Chopsticks - In About A Minute 🍜.mp4"
video_file = open(video_path, "rb")

transcript = Functions.Transcription.whisper(api_key, video_file)
cleanNotes = Functions.NotesMaker.gpt(api_key, transcript)

print(cleanNotes)