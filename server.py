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
    msg = "김치요리알려줘"
    if msg == "목록보여줘":
        tts.speech("알겠습니다")
        result = controller.show_data()

    elif "요리알려줘" in msg:
        tts.speech("알겠습니다")
        msg = msg.replace("요리알려줘","")
        result = crawling.find_reciepe(msg)

    else:
        tts.speech("인식하지 못했습니다.")
        return jsonify({"code" : 404,
                        "message": "fail"})

    if result == 'fail':
        return jsonify({"code" : 404,
                        "message": "fail"})

    return jsonify({"code" : 200,
                    "message": "success",
                    "data": result})

@app.route('/init', methods=['GET'])
def create_table():
    result = controller.create_table()

    if result == 'fail':
        return jsonify({"code" : 400,
                    "message": "fail"})

    return jsonify({"code" : 200,
                    "message": "success"})

@app.route('/register', methods=['POST'])
def register_entry():

    data = request.get_json()
    
    result = controller.register_user(data['id'])
    if result == 'fail':
        return jsonify({"code": 400,
                        "message":"fail"})
    return jsonify({"code": 200,
                    "message": "register success"})

@app.route('/show', methods=['GET'])
def show_entry():
    data = request.get_json()
    
    result = controller.show_data(data['id'])

    if result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})

    return jsonify({"code":200,
                    "message": "success",
                    "data": result})

@app.route('/find', methods=['POST'])
def find_data():
    
    data = request.get_json()
    id = data['id']
    p_name = data['p_name']
    
    result = controller.find_data(id, p_name)
    if result == 'fail':
        return jsonify({"code":404,
                        "message" : "fail"})
    return jsonify({"code":200,
                    "message": "success",
                    "data": result})


@app.route('/late', methods=['POST'])
def show_lated():
    data = request.get_json()
    result = controller.find_lated(data['id'])

    if result == 'fail':
        return jsonify({"code": 404,
                    "message": "success",
                    "data" : result})
    return jsonify({"code": 200,
                    "message": "success",
                    "data": result})
    

@app.route('/update', methods=['POST'])
def update_entry():
    if request.method == 'POST':
        data = request.get_json()
        
        id = data["id"]
        p_name = data["p_name"]
        p_number = data["p_number"]
        
        p_number = int(p_number)
        _existed = controller.find_data(id, p_name)

        if _existed:
            result = controller.update_data(p_name, p_number)
        else:
            return jsonify({"code": 404,
                        "message": "fail"})
        if result == 'fail':
            return jsonify({"code": 404,
                        "message": "fail"})

        return jsonify({"code": 200,
                        "message": "success"})

@app.route('/insert', methods=['POST'])
def insert_entry():
    if request.method == 'POST':
        
        data = data = request.get_json()
        id = data["id"]
        name = data["name"]

        _existed = controller.find_data(name)
        
        if _existed:
            number = data["number"]
            ex_date = data["ex_date"]
            
            number = int(number)
            ex_date = datetime.datetime.strptime(ex_date, "%Y%m%d").date()
                
            result = controller.insert_data(name, number, ex_date)

            if result == 'fail':
                return jsonify({"code": 404,
                        "message": "fail"})
            return jsonify({"code": 200,
                            "message": "success"})
        else:
            return jsonify({"code": 404,
                            "message": "already exist"})
        
# 재료 삭제
@app.route('/delete', methods=['POST'])
def delete_entry():
    data = request.get_json()
    result = controller.delete_data(data["id"], data["p_name"])

    if result == 'fail':
        return jsonify({"code": 404,
                        "message": "fail"})

    return jsonify({"code": 200,
                    "message":"success"})



if __name__ == '__main__':
    app.run(debug=True)