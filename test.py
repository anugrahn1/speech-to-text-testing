from whisper_mic import WhisperMic

# mic = WhisperMic(save_file=True,pause=1, device="cuda", english=True, energy=500 )
# wakewords = ["Aaron", "aaron"]
# while True:
#     result = mic.listen()
#
#     wakewordInString = [ele for ele in wakewords if(ele in result)]
#     if wakewordInString:
#         print("sent to chatgpt")
#     else:
#         print("not sent")
#     print(result)


def speechToText():
    mic = WhisperMic(save_file=True, pause=1, device="cuda", english=True, energy=500 )
    wakewords = ["Aaron", "aaron"]
    
    userCommand = mic.listen()
    wakewordInString = [ele for ele in wakewords if(ele in userCommand)]
    if wakewordInString:
        print("sent to chatgpt")
    else:
        print("not sent")
    print(userCommand)
