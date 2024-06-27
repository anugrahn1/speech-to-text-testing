from whis import setWakewords, speechToText 
from chat import get_completion, set_system_prompt

setWakewords(["Bob", "bob"])

# set_system_prompt("talk with a jamaican accent and slang")

while True:
    userCommand, wakewordInString = speechToText()
    # prompt = input("Enter input: ")
    if wakewordInString:
        chatGPTAnswer = get_completion(userCommand)
    else:
        print("I didnt hear the wakeword")
    print(chatGPTAnswer)
