from whisper_mic import WhisperMic

wakewords = ["Aaron", "aaron"]

def setWakewords(wakewordList):
   global wakewords  
   wakewords = wakewordList

def speechToText():
    mic = WhisperMic(save_file=True, pause=1, device="cuda", english=True, energy=4000, dynamic_energy=False )
    
    userCommand = mic.listen()
    wakewordInString = [ele for ele in wakewords if(ele in userCommand)]
    if wakewordInString:
        print("sent to chatgpt")
    else:
        print("not sent")
    return userCommand, wakewordInString
