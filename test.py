from whisper_mic import WhisperMic

mic = WhisperMic()
result = mic.listen()

wakewords = ["Aaron", "aaron"]
res = [ele for ele in wakewords if(ele in result)]
if res:
    print("sent to chatgpt")
else:
    print("not sent")
print(result)