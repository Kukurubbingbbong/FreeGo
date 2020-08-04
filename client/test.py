import recognition
import tts
import requests
import crawling

def runSpeechRecogizer():
    msg = recognition.voice_recognize()
    msg = msg = msg.replace(" ","")
    print("input message: [{}]".format(msg))

    if msg == "목록보여줘":
        tts.speech("알겠습니다")
        body = {'id' : '내 냉장고1'}
        res = requests.post('localhost:5000/show', data=body)
        print(res)
    elif "요리알려줘" in msg:
        tts.speech("알겠습니다")
        msg = msg.replace("요리알려줘","")
        res = crawling.find_reciepe(msg)
        print(res)
    elif "있어" in msg:
        msg = msg.replace("있어","")
        body = {'id' : '내 냉장고1', 'p_name' : "오이" }
        res = requests.post('127.0.0.1:5000/find', data=body)
        print(res)
    else:
        tts.speech("인식하지 못했습니다.")
        return "fail"
