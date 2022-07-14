import requests
import json
import pyttsx3 

url = "http://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
response = requests.get(url) 
print(response.status_code)

jsonData = json.loads(response.text)
print(jsonData["joke"])

engine = pyttsx3.init()
engine.setProperty('rate', 150) 
engine.say(jsonData["joke"])
engine.runAndWait()