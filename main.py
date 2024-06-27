from test import speechToText
from chat import get_completion, set_system_prompt



# set_system_prompt("talk with a jamaican accent and slang")

while True:
    userCommand = speechToText()
    # prompt = input("Enter input: ")
    chatGPTAnswer = get_completion(userCommand)
    print(chatGPTAnswer)
