from whis import setWakewords, speechToText 
from chat import get_completion, set_system_prompt
from eleven import text_to_speech_file, play_new_mp3_files, play_mp3_files, delete_mp3_files 
import pygame
import os
from colorama import Fore, Back, Style

setWakewords(["Bob", "bob", "Aaron", "aaron", "erin", "Erin"])

set_system_prompt("You are Aaron, a very knowledgable college professor who is helpful and straight forward, use exclamation marks when your opinion is strong. You are directly speaking to the user, do not use bullet points or lists")
PATH = r'C:\Users\Georg\speech-to-text-testing'
try:
    delete_mp3_files(PATH)
except:
    pass 

while True:
    userCommand, wakewordInString = speechToText()

    userCommand = userCommand.lower()
    if wakewordInString:
        if "devil" in userCommand or "advocate" in userCommand:
            print(Fore.RED + 'DEVILS ADVOCATE MODE!!! >:(')
            print(Style.RESET_ALL)
            set_system_prompt("You are named Aaron, you are very straightforward and confident. You make no mistakes and are always opposing the user's views and offering a different opinion. Your job is to play the devil's advocate. Always respond with exclamation marks at the end of your sentences to show that you are always angry.")

        if "normal" in userCommand:
            print(Fore.CYAN + "Normal Mode :) ")
            print(Style.RESET_ALL)
            set_system_prompt("You are Aaron, a very knowledgable college professor who is helpful and straight forward, use exclamation marks when your opinion is strong. You are directly speaking to the user, do not use bullet points or lists")
        
    if wakewordInString:
        chatGPTAnswer = get_completion(userCommand)
        print(chatGPTAnswer)
        text_to_speech_file(str(chatGPTAnswer))
        play_new_mp3_files(PATH)
    else:  
        print("I didnt hear the wakeword")
