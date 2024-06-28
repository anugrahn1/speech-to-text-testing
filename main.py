from whis import setWakewords, speechToText 
from chat import get_completion, set_system_prompt
from eleven import text_to_speech_file, play_new_mp3_files, delete_mp3_files 
# import pygame
# import os
from colorama import Fore, Style
from datetime import datetime

setWakewords(["Bob", "bob", "Aaron", "aaron", "erin", "Erin"])

set_system_prompt("You are Aaron, a very knowledgable college professor who is helpful and straight forward, use exclamation marks when your opinion is strong. You are directly speaking to the user, do not use bullet points or lists. ")
PATH = r'C:\Users\Georg\speech-to-text-testing'
try:
    delete_mp3_files(PATH)
except:
    pass 
evilMode = False 
while True:
    now = datetime.now()
    time = str(now.time()).split('.', 1)[0]
    temperature = 78
    weather_condition = "sunny"
    if not evilMode:
        set_system_prompt(f'''You are Aaron or Erin, a very knowledgable college professor who is helpful and straight forward, use exclamation marks when your opinion is strong. You are directly speaking to the user, do not use bullet points or lists. If asked for time say it is {time}. If you are
                          asked for the weather, say it is {temperature} degrees and the weather conditions are {weather_condition}.''')
    userCommand, wakewordInString = speechToText()

    userCommand = userCommand.lower()
    if wakewordInString:
        if "devil" in userCommand or "advocate" in userCommand:
            print(Fore.RED + 'DEVILS ADVOCATE MODE!!! >:(')
            print(Style.RESET_ALL)
            set_system_prompt("You are named Aaron or Erin, you are very straightforward and confident. You make no mistakes and are always opposing the user's views and offering a different opinion. Your job is to play the devil's advocate. Always respond with exclamation marks at the end of your sentences to show that you are always angry.")
            evilMode = True

        if "normal" in userCommand:
            print(Fore.CYAN + "Normal Mode :) ")
            print(Style.RESET_ALL)
            set_system_prompt(f"You are Aaron, a very knowledgable college professor who is helpful and straight forward, use exclamation marks when your opinion is strong. You are directly speaking to the user, do not use bullet points or lists. If asked for time say it is {time}")
            evilMode = False

    if wakewordInString:
        chatGPTAnswer = get_completion(userCommand)
        print(chatGPTAnswer)
        text_to_speech_file(str(chatGPTAnswer))
        play_new_mp3_files(PATH)
    else:  
        print("I didnt hear the wakeword")
