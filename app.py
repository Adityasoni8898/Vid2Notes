import openai

api_key = "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"
openai.api_key = api_key

messages = [{"role":"system", "content":"You are a teacher teaching english, max word limit fifty words"}]

print("Your teacher is ready")
while input!= "quit()":
    message = input()
    messages.append({"role": "user", "content":message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"] [0] ["message"] ["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")


#whisper
# model_id = 'whisper-1'

# media_file_path = 'path'
# media_file = open(media_file_path)

# response = openai.Audio.transcribe(
#     api_key = api_key,
#     model = model_id,
#     file = media_file,
#     response_format = 'srt' 
# )