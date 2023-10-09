import openai

def gpt(api_key, transcript):

    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "user", "content" : "convert this transcribed text from a tutorial into good simple notes, chapter wise"},
            {"role" : "user", "content" : transcript }
        ]
    )

    return response.choices[0].message.content