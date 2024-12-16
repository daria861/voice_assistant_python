import time
import random
import requests
from output import say, engine
import speech_recognition as sr


def get_time(text:str):
    
    current_time = time.localtime()
    
    output_time = f'{current_time.tm_hour}:{current_time.tm_min}'
    return {"time":output_time}

def get_random_number(text:str):
    return {"number": random.randint(0, 100)}

def get_random_flip(text: str):
    variants = ["head", "tail"]
    
    winner = random.choice(variants)
    
    if winner == "head":
        return {"winner_side": "head", "loser_side":"tail"}
    else:
        return {"winner_side": "tail", "loser_side":"head"}
    
    
    
def get_dollar_rate(text:str):
    result = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    result = result.json()
    total = str(round(float(result[1]['sale']),2))
    total = total.split('.')
    return {"uah_rate": total[0], "coin_rate": total[1]}


def game(text:str):
    recognizer = sr.Recognizer()
    say("Ok. Let's play. Guess a number from 0 to 100. Say a stop if you want to stop game")
    correct_number = random.randint(0, 100)
    with sr.Microphone() as source:
        print('ready game')
        while True:
            engine.runAndWait()
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            #try-except errors
            try:
                text = recognizer.recognize_google(audio, language='en-GB')
                print(f"You said: {text}")
                if text.isdigit():
                    number_user = int(text)
                    if number_user == correct_number:
                        say("Congratulations, this is the correct number")
                        break
                    elif number_user < correct_number:
                        say(f"Try again. My number is greater then {number_user}")
                    elif number_user > correct_number:
                        say(f"Try again. My number is less then {number_user}")
                elif "stop" in text:
                    break
                else:
                    say("You need say only number")
            except sr.UnknownValueError:
                print("Audio is not recognized")
            except sr.RequestError:
                print("request error")       
            except sr.WaitTimeoutError:
                print("wait timeout")
    return {}