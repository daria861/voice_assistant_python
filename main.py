import speech_recognition as sr
from output import say, engine
import json
import random
from functions import * 



def load_speech():
    with open("speech.json", 'r') as file:
        data = json.load(file)
    return data


def speech_commands(text:str):
    data = load_speech()
    result = False
    for phrase in data:
        for input_words in phrase['input']:
            if input_words in text.lower():
                output = random.choice(phrase['output'])
                function_name = phrase.get("function")
                print(function_name)
                if function_name:
                    func = globals().get(function_name)
                    if func:
                        output_func = func(text)
                        for key in output_func.keys():
                            output = output.replace(f'[{key}]', str(output_func[key]))
                say(output)
                print(output)
                result = True
    return result

# obtain audio from the microphone
def main():
    
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        
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
                variants = [
                        "I don't understand you",
                        "Sorry, I did not get it",
                        "Repeat, please"
                    ]
                say(random.choice(variants)) 
            except sr.RequestError:
                print("request error")       
            except sr.WaitTimeoutError:
                print("wait timeout")
            
main()