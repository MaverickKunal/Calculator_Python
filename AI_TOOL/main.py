import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
from config import api_key


chatstr = ""
def chat(text):
    global chatstr
    openai.api_key = api_key
    chatstr += f"Kunal : {text} \n Chatbot :"
    print(chatstr)

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        say(response["choices"][0]["text"])
        chatstr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]

    except Exception as e:
        return "AI Error"

def AI(prompt):
    openai.api_key = api_key
    text = f"AI Bot response for prompt: {prompt} \n **************** \n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai Files"):
            os.mkdir("Openai Files")

        with open(f"Openai Files/{''.join(prompt.split('chatbot')[1:]).strip()}.txt", "w") as f:
            f.write(text)

    except Exception as e:
        return "AI Error"

def say(text):
    os.system(f"say {text}")

def Take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language = "en-in")
            #print(f"User said: {query}")
            return query
        except Exception as e:
            return "Voice not recognized"


if __name__ != '__main__':
    pass
else:
    print('Julie A.I. Bot')
    say("Hello this is Julie A.I., how may I help you")
    while True:
        print("listening,....")
        text = Take_Command()
        say(text)
        sites = [["Mahadev","https://www.hotstar.com/in/shows/devon-ke-dev-mahadev/12"],["dark desire", "https://www.netflix.com/search?q=dark%20desire&jbv=81090319"],["Chat Gpt","https://chat.openai.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                #say("Mahadev Hotstar opening for you....")
                say(f"Here is your {site[0]}..., enjoy, tadaaaaaaaa!!")
                #webbrowser.open("https://www.hotstar.com/in/shows/devon-ke-dev-mahadev/12")
                webbrowser.open(site[1])

        if "current time" in text:
                t = datetime.datetime.now().strftime("%H")
                m = datetime.datetime.now().strftime("%M")
                say(f"Bro the current time is {t} hours and {m} minutes")

        elif "open Facetime".lower() in text.lower():
            fc_path = "/system/Applications/FaceTime.app"
            os.system(f"open {fc_path}")

        elif "using chatbot".lower() in text.lower():
            AI(prompt=text)

        elif "Julie quit".lower() in text.lower():
            exit()

        else:
            print("chatting with Julie A.I. Bot")
            chat(text)