import pyttsx3

engine = pyttsx3.init()

# print(engine.getProperty("voice"))

def say(text):
    engine.say(text)