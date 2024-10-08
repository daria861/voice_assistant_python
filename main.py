import speech_recognition as sr
from output import say, engine
import json
import random



def load_speech():
    with open("speech.json", 'r') as file:
        data = json.load(file)
    return data

data = load_speech()

def speech_commands(text:str):
    for phrase in data:
        for input_words in phrase['input']:
            if input_words in text.lower():
                output = random.choice(phrase['output'])
                say(output)
                print(output)
            

# obtain audio from the microphone
def main():
    
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        # say("Hello, I am your voice assistant. How can I help you?")
        
        while True:
            engine.runAndWait()
            print("Say something! Listening.........")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            #try-except errors
            try:
                text = recognizer.recognize_google(audio, language='en-GB')
                print(f"You said: {text}")
                speech_commands(text)
            except sr.UnknownValueError:
                print("Audio is not recognized")   
            except sr.RequestError:
                print("request error")       
            except sr.WaitTimeoutError:
                print("wait timeout")
            
main()
