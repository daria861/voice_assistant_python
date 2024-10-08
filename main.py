import speech_recognition as sr

from output import say, engine




# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))



# obtain audio from the microphone
def main():
    
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        say("Hello, I am your voice assistant. How can I help you?")
        engine.runAndWait()
        
        while True:
            
            print("Say something! Listening.........")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            #try-except errors
            try:
                text = recognizer.recognize_google(audio, language='en-GB')
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Audio is not recognized")   
            except sr.RequestError:
                print("request error")       
            except sr.WaitTimeoutError:
                print("wait timeout")
            
main()
