from flask import Flask, request
import recognition 

app = Flask(__name__)

@app.route('/speech',methods=['GET'])
def runSpeechRecogizer():
    msg = recognition.voice_recognize()

    data = {
        "ingredient" : [
            {
                "name" : "가지",
                "storage" : 1,
                "ex_date" : "2020-7-8"
            },
            {
                "name" : "수박",
                "storage" : 3,
                "ex_date" : "2020-7-8"
            },
            {
                "name" : "오이",
                "storage" : 7,
                "ex_date" : "2020-7-8"
            }
        ]
    }
    print(msg)
    if "보여 줘" in msg:
        print(data)
    return "success"

if __name__ == "__main__":
    app.run(debug=True)    