from flask import Flask, request, jsonify
import json
import recognition
import crawling
import tts
import orm.controller as controller
import datetime


app = Flask(__name__)


@app.route('/speech',methods=['GET'])
def runSpeechRecogizer():
    msg = recognition.voice_recognize()
    msg = msg = msg.replace(" ","")
    print("input message: [{}]".format(msg))

    if msg == "목록보여줘":
        tts.speech("알겠습니다")
        result = controller.show_data()

    elif "요리알려줘" in msg:
        tts.speech("알겠습니다")
        msg = msg.replace("요리알려줘","")
        result = crawling.find_reciepe(msg)
    else:
        tts.speech("인식하지 못했습니다.")
        result = "fail"

    return jsonify({"result": result})

@app.route('/initdatabase', methods=['GET'])
def create_table():
    result = controller.create_table()
    return jsonify({"result": result})
    

@app.route('/show', methods=['GET'])
def showList():
    result = controller.show_data()
    return jsonify({"result": result})

@app.route('/late', methods=['GET'])
def showlated():
    result = controller.find_lated()
    return jsonify({"result":result})


@app.route('/update', methods=['POST'])
def update_entry():
    if request.method == 'POST':
        data = request.get_json()
        name = data["name"]
        number = data["number"]
        
        number = int(number)
        _existed = controller.find_data(name)

        if _existed:
            ex_date = data["ex_date"]
            ex_date = datetime.datetime.strptime(ex_date, "%Y%m%d").date()
            
            result = controller.insert_data(name, number, ex_date)
        else:
            result = controller.update_data(name, number)

        return jsonify({"result": result})

@app.route('/delete', methods=['POST'])
def delete_entry():
    data = request.get_json()
    controller.delete_data(data["name"])

if __name__ == '__main__':
    app.run(debug=True)