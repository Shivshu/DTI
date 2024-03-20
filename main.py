import os
import pygame
import speech_recognition as sr
from bot_scrapper import *
import pyautogui


def speak(text):
    voice = "en-US-AriaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    os.system(command)
    
    pygame.init()
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("output.mp3")
        
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(e)
        
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
   
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        
    except Exception as e:
        print(e)
        return ""
    return query
    
# speak("hello i am your ChatterBot assistant. How can i assist you today!")
# query = take_command()
# print(query)

while True:
    query = take_command().lower()
    print('You: ' + query)
    
    if "hello" in query:
        speak("hi how are you")
    elif 'i am fine' in query:
        speak('thats great to hear')
    else:
        speak("I dont understand")
        

while True:
    query = take_command().lower()
    
    print('\n You: ' + query)
    
    if open in query:
        
        app_name = query.replace('open', '')
        
        speak('opening '+ app_name)
        
        pyautogui.press('super')
        pyautogui.typewriter(app_name)
        pyautogui.sleep(0.7)
        pyautogui.press('enter')
        
    
    elif 'switch tab' in query:
        
        pyautogui.hotkey('ctrl', 'tab')
        
        
    elif 'close tab' in query:
        
        pyautogui.hotkey('ctrl', 'w')
        
        
    elif 'close' in query:
        
        pyautogui.hotkey ('alt', 'f4')
        speak('done sir')
        
        
    elif 'time' in query:
        
        current_time = datetime.now().strftime('%H:%M %p')
        speak('Current time is '+ current_time)
    
 
    
    elif 'close' in query:
        
        pyautogui.hotkey('alt', 'f4')
        speak('Done Sir!')
        
    elif 'play' in query:
        
        song_name = query.replace('play', '')
        speak('Sure sir. Playing'+ song_name + 'in youtube')
        pywhatkit.playonyt(song_name)
        
        
        
    elif 'sleep' in query:
        speak('ok sir. sleep_mode going to sleep but you can call me any time just say wake up and i will be there for you.')
        sleep_mode = True
    
    
    else:
        
        sendQuery(query)
        isBubbleloaderVisible()
        response = retriveData()
        speak(response)
    
    
    while sleep_mode:
        query = take_command().lower()
# import os
# import pygame
# import speech_recognition as sr

# def speak(text):
#     voice = "en-US-AriaNeural"
#     command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
#     os.system(command)
    
#     pygame.init()
#     pygame.mixer.init()
    
#     try:
#         pygame.mixer.music.load("output.mp3")
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
            
#     except Exception as e:
#         print(e)
        
#     finally:
#         pygame.mixer.music.stop()
#         pygame.mixer.quit()
   
# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
        
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-us')
        
#     except Exception as e:
#         print(e)
#         return ""
#     return query
    
# # speak("hello i am your ChatterBot assistant. How can i assist you today!")

# while True:
#     query = take_command().lower()  # Call lower() method correctly
#     print("You: " + query)
    
#     if "hello" in query or 'hi' in query:
#         speak("hi how are you")
#     elif 'i am fine' in query:
#         speak('thats great to hear')
#     else:
#         speak("I dont understand")