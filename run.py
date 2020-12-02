from flask import Flask, render_template, jsonify
from random import *
import time
import json
from kafka import KafkaConsumer

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

lineHistory = []


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    consumer = KafkaConsumer('hot', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    for msg in consumer:
        num = (msg.value).decode('utf8')
        i += 1
        if i > 0 and msg is not None:
            break
    response = {
        'randomNumber': num
    }
    return jsonify(response)


@app.route('/api/answer')
def get_answer():
    consumer = KafkaConsumer('answer', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "":
            break
    resList = []
    returnList = []
    resList = result.split(",")
    for item in resList:
        temp_dict = {}
        temp_list = item.split(":")
        temp_dict['state'] = temp_list[0][1:-1]
        temp_dict['number'] = int(temp_list[1])
        returnList.append(temp_dict)
    returnJson = json.dumps(returnList)
    return returnJson


@app.route('/api/count')
def get_count():
    consumer = KafkaConsumer('stateTag', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "":
            break
    resList = []
    returnList = []
    resList = result.split(",")
    for item in resList:
        temp_dict = {}
        temp_list = item.split(":")
        temp_dict['word'] = temp_list[0][1:-1]
        temp_dict['count'] = int(temp_list[1])
        returnList.append(temp_dict)
    returnJson = json.dumps(returnList)
    return returnJson


@app.route('/api/location')
def get_location():
    consumer = KafkaConsumer('location', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "":
            break
    resList = []
    returnList = []
    resList = result.split(",")
    for item in resList:
        if item[0:2] == '\"\"':
            continue
        temp_dict = {}
        temp_list = item.split(":")
        temp_dict['number'] = int(temp_list[-1])
        temp_temp_list = temp_list[0][1:-1].split('+')
        temp_dict['lat'] = float(temp_temp_list[1])
        temp_dict['lng'] = float(temp_temp_list[0])
        returnList.append(temp_dict)
    returnJson = json.dumps(returnList)
    return returnJson


@app.route('/api/barchart')
def get_bar():
    consumer = KafkaConsumer('noStateTag', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "" and result.split(",")[0].split(":")[1] != '0':
            break
    returnList = []
    resList = result.split(",")
    for item in resList:
        temp_dict = {}
        temp_list = item.split(":")
        temp_dict['language'] = temp_list[0][1:-1]
        temp_dict['number'] = int(temp_list[1])
        if len(returnList) == 5:
            break
        returnList.append(temp_dict)
    returnJson = json.dumps(returnList)
    return returnJson


@app.route('/api/funnel')
def get_funnel():
    consumer = KafkaConsumer('editor', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "":
            break
    resList = []
    returnList = []
    resList = result.split(",")
    temp_dict1 = {'range': '0~500', 'number': 0}
    temp_dict2 = {'range': '500~5000', 'number': 0}
    temp_dict3 = {'range': '5000~10000', 'number': 0}
    temp_dict4 = {'range': 'Over 10000', 'number': 0}
    for item in resList:
        temp_list = item.split(":")
        temp_num = int(temp_list[0][1:-1])
        if 0 < temp_num < 500:
            temp_dict1['number'] += 1
        elif 500 < temp_num < 5000:
            temp_dict2['number'] += 1
        elif 5000 < temp_num < 10000:
            temp_dict3['number'] += 1
        elif 10000 < temp_num:
            temp_dict4['number'] += 1
    returnList.append(temp_dict1)
    returnList.append(temp_dict2)
    returnList.append(temp_dict3)
    returnList.append(temp_dict4)
    returnJson = json.dumps(returnList)
    return returnJson


@app.route('/api/line')
def get_line():
    global lineHistory
    consumer = KafkaConsumer('noStateTag', bootstrap_servers=['49.235.251.50:9092'])
    i = 0
    ticks = time.time()
    timeArray = time.localtime(ticks)
    res = time.strftime("%H:%M:%S", timeArray)
    line_dict = {'time': res, 'C': 0, 'Java': 0, 'Python': 0}
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "":
            break
    resList = result.split(",")
    for item in resList:
        temp_list = item.split(":")
        lan = temp_list[0][1:-1]
        if lan.startswith("C") or lan.startswith("c"):
            line_dict['C'] += int(temp_list[1])
        elif lan.startswith("python") or lan.startswith("Python"):
            line_dict['Python'] += int(temp_list[1])
        elif lan.startswith("java") or lan.startswith("Java"):
            line_dict['Java'] += int(temp_list[1])
    if len(lineHistory) > 8:
        del lineHistory[0]
    if line_dict['Java'] != 0 and line_dict['Python'] != 0 and line_dict['C'] != 0:
        lineHistory.append(line_dict)
    return json.dumps(lineHistory)


if __name__ == '__main__':
    app.run()
