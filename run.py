from flask import Flask, render_template, jsonify
from random import *
import time
import json
from kafka import KafkaConsumer

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


def background():
    global num


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    consumer = KafkaConsumer('hot', bootstrap_servers=['188.131.179.244:9092'])
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


@app.route('/api/world')
def get_words():
    response = {
        "status": True,
        "namemap": {
            "Afghanistan": "Afghanistan",
            "Angola": "Angola",
            "Albania": "Albania",
            "Algeria": "Algeria",
            "Argentina": "Argentina",
            "Armenia": "Armenia",
            "Australia": "Australia",
            "Austria": "Austria",
            "Azerbaijan": "Azerbaijan",
            "Bahamas": "Bahamas",
            "Bangladesh": "Bangladesh",
            "Belgium": "Belgium",
            "Benin": "Benin",
            "Burkina Faso": "Burkina Faso",
            "Burundi": "Burundi",
            "Bulgaria": "Bulgaria",
            "Bosnia and Herz.": "Bosnia and Herz.",
            "Belarus": "Belarus",
            "Belize": "Belize",
            "Bermuda": "Bermuda",
            "Bolivia": "Bolivia",
            "Brazil": "Brazil",
            "Brunei": "Brunei",
            "Bhutan": "Bhutan",
            "Botswana": "Botswana",
            "Cambodia": "Cambodia",
            "Cameroon": "Cameroon",
            "Canada": "Canada",
            "Central African Rep.": "Central African Rep.",
            "Chad": "Chad",
            "Chile": "Chile",
            "China": "China",
            "Colombia": "Colombia",
            "Congo": "Congo",
            "Costa Rica": "Costa Rica",
            "Côte d'Ivoire": "Côte d'Ivoire",
            "Croatia": "Croatia",
            "Cuba": "Cuba",
            "Cyprus": "Cyprus",
            "Czech Rep.": "Czech Rep.",
            "Dem. Rep. Korea": "Dem. Rep. Korea",
            "Dem. Rep. Congo": "Dem. Rep. Congo",
            "Denmark": "Denmark",
            "Djibouti": "Djibouti",
            "Dominican Rep.": "Dominican Rep.",
            "Ecuador": "Ecuador",
            "Egypt": "Egypt",
            "El Salvador": "El Salvador",
            "Eq. Guinea": "Eq. Guinea",
            "Eritrea": "Eritrea",
            "Estonia": "Estonia",
            "Ethiopia": "Ethiopia",
            "Falkland Is.": "Falkland Is.",
            "Fiji": "Fiji",
            "Finland": "Finland",
            "France": "France",
            "French Guiana": "French Guiana",
            "Fr. S. Antarctic Lands": "Fr. S. Antarctic Lands",
            "Gabon": "Gabon",
            "Gambia": "Gambia",
            "Germany": "Germany",
            "Georgia": "Georgia",
            "Ghana": "Ghana",
            "Greece": "Greece",
            "Greenland": "Greenland",
            "Guatemala": "Guatemala",
            "Guinea": "Guinea",
            "Guinea-Bissau": "Guinea-Bissau",
            "Guyana": "Guyana",
            "Haiti": "Haiti",
            "Heard I. and McDonald Is.": "Heard I. and McDonald Is.",
            "Honduras": "Honduras",
            "Hungary": "Hungary",
            "Iceland": "Iceland",
            "India": "India",
            "Indonesia": "Indonesia",
            "Iran": "Iran",
            "Iraq": "Iraq",
            "Ireland": "Ireland",
            "Israel": "Israel",
            "Italy": "Italy",
            "Ivory Coast": "Ivory Coast",
            "Jamaica": "Jamaica",
            "Japan": "Japan",
            "Jordan": "Jordan",
            "Kashmir": "Kashmir",
            "Kazakhstan": "Kazakhstan",
            "Kenya": "Kenya",
            "Kosovo": "Kosovo",
            "Kuwait": "Kuwait",
            "Kyrgyzstan": "Kyrgyzstan",
            "Laos": "Laos",
            "Lao PDR": "Lao PDR",
            "Latvia": "Latvia",
            "Lebanon": "Lebanon",
            "Lesotho": "Lesotho",
            "Liberia": "Liberia",
            "Libya": "Libya",
            "Lithuania": "Lithuania",
            "Luxembourg": "Luxembourg",
            "Madagascar": "Madagascar",
            "Macedonia": "Macedonia",
            "Malawi": "Malawi",
            "Malaysia": "Malaysia",
            "Mali": "Mali",
            "Mauritania": "Mauritania",
            "Mexico": "Mexico",
            "Moldova": "Moldova",
            "Mongolia": "Mongolia",
            "Montenegro": "Montenegro",
            "Morocco": "Morocco",
            "Mozambique": "Mozambique",
            "Myanmar": "Myanmar",
            "Namibia": "Namibia",
            "Netherlands": "Netherlands",
            "New Caledonia": "New Caledonia",
            "New Zealand": "New Zealand",
            "Nepal": "Nepal",
            "Nicaragua": "Nicaragua",
            "Niger": "Niger",
            "Nigeria": "Nigeria",
            "Korea": "Korea",
            "Northern Cyprus": "Northern Cyprus",
            "Norway": "Norway",
            "Oman": "Oman",
            "Pakistan": "Pakistan",
            "Panama": "Panama",
            "Papua New Guinea": "Papua New Guinea",
            "Paraguay": "Paraguay",
            "Peru": "Peru",
            "Republic of the Congo": "Republic of the Congo",
            "Philippines": "Philippines",
            "Poland": "Poland",
            "Portugal": "Portugal",
            "Puerto Rico": "Puerto Rico",
            "Qatar": "Qatar",
            "Republic of Serbia": "Republic of Serbia",
            "Romania": "Romania",
            "Russia": "Russia",
            "Rwanda": "Rwanda",
            "Samoa": "Samoa",
            "Saudi Arabia": "Saudi Arabia",
            "Senegal": "Senegal",
            "Serbia": "Serbia",
            "Sierra Leone": "Sierra Leone",
            "Slovakia": "Slovakia",
            "Slovenia": "Slovenia",
            "Solomon Is.": "Solomon Is.",
            "Somaliland": "Somaliland",
            "Somalia": "Somalia",
            "South Africa": "South Africa",
            "S. Geo. and S. Sandw. Is.": "S. Geo. and S. Sandw. Is.",
            "S. Sudan": "S. Sudan",
            "Spain": "Spain",
            "Sri Lanka": "Sri Lanka",
            "Sudan": "Sudan",
            "Suriname": "Suriname",
            "Swaziland": "Swaziland",
            "Sweden": "Sweden",
            "Switzerland": "Switzerland",
            "Syria": "Syria",
            "Tajikistan": "Tajikistan",
            "Tanzania": "Tanzania",
            "Thailand": "Thailand",
            "Timor-Leste": "Timor-Leste",
            "Togo": "Togo",
            "Trinidad and Tobago": "Trinidad and Tobago",
            "Tunisia": "Tunisia",
            "Turkey": "Turkey",
            "Turkmenistan": "Turkmenistan",
            "Uganda": "Uganda",
            "Ukraine": "Ukraine",
            "United Arab Emirates": "United Arab Emirates",
            "United Kingdom": "United Kingdom",
            "United Republic of Tanzania": "United Republic of Tanzania",
            "United States": "United States",
            "United States of America": "United States of America",
            "Uruguay": "Uruguay",
            "Uzbekistan": "Uzbekistan",
            "Vanuatu": "Vanuatu",
            "Venezuela": "Venezuela",
            "Vietnam": "Vietnam",
            "West Bank": "West Bank",
            "W. Sahara": "W. Sahara",
            "Yemen": "Yemen",
            "Zambia": "Zambia",
            "Zimbabwe": "Zimbabwe"
        },
        "dataArr": [
            {
                "name": "阿富汗",
                "value": 28397.812
            },
            {
                "name": "安哥拉",
                "value": 19549.124
            },
            {
                "name": "阿尔巴尼亚",
                "value": 3150.143
            },
            {
                "name": "阿尔及利亚",
                "value": 8441.537
            },
            {
                "name": "阿根廷",
                "value": 40374.224
            },
            {
                "name": "亚美尼亚",
                "value": 2963.496
            },
            {
                "name": "澳大利亚",
                "value": 268.065
            },
            {
                "name": "奥地利",
                "value": 22404.488
            },
            {
                "name": "阿塞拜疆",
                "value": 8401.924
            },
            {
                "name": "布隆迪",
                "value": 9094.718
            },
            {
                "name": "比利时",
                "value": 9232.753
            },
            {
                "name": "贝宁",
                "value": 10941.288
            },
            {
                "name": "布基纳法索",
                "value": 9509.798
            },
            {
                "name": "孟加拉国",
                "value": 15540.284
            },
            {
                "name": "保加利亚",
                "value": 151125.475
            },
            {
                "name": "波斯尼亚和黑塞哥维那",
                "value": 7389.175
            },
            {
                "name": "白俄罗斯",
                "value": 66402.316
            },
            {
                "name": "伯利兹",
                "value": 3845.929
            },
            {
                "name": "百慕大群岛",
                "value": 9491.07
            },
            {
                "name": "玻利维亚",
                "value": 308.595
            },
            {
                "name": "巴西",
                "value": 64.951
            },
            {
                "name": "文莱",
                "value": 716.939
            },
            {
                "name": "不丹",
                "value": 195210.154
            },
            {
                "name": "博茨瓦纳",
                "value": 27.223
            },
            {
                "name": "柬埔寨",
                "value": 716.939
            },
            {
                "name": "喀麦隆",
                "value": 1969.341
            },
            {
                "name": "加拿大",
                "value": 4349.921
            },
            {
                "name": "中非共和国",
                "value": 34126.24
            },
            {
                "name": "乍得",
                "value": 7830.534
            },
            {
                "name": "智利",
                "value": 17150.76
            },
            {
                "name": "中国",
                "value": 1359821.465
            },
            {
                "name": "哥伦比亚",
                "value": 60508.978
            },
            {
                "name": "刚果",
                "value": 17150.343
            },
            {
                "name": "科特迪瓦",
                "value": 17150.343
            },
            {
                "name": "哥斯达黎加",
                "value": 20624.343
            },
            {
                "name": "克罗地亚",
                "value": 62191.161
            },
            {
                "name": "古巴",
                "value": 3573.024
            },
            {
                "name": "塞浦路斯",
                "value": 46444.798
            },
            {
                "name": "捷克共和国",
                "value": 4669.685
            },
            {
                "name": "民主刚果",
                "value": 11281.768
            },
            {
                "name": "丹麦",
                "value": 1.468
            },
            {
                "name": "吉布提",
                "value": 1103.685
            },
            {
                "name": "多米尼加共和国",
                "value": 10553.701
            },
            {
                "name": "东帝汶",
                "value": 83017.404
            },
            {
                "name": "厄瓜多尔",
                "value": 834.036
            },
            {
                "name": "埃及",
                "value": 5550.959
            },
            {
                "name": "萨尔瓦多",
                "value": 10016.797
            },
            {
                "name": "赤道几内亚",
                "value": 37062.82
            },
            {
                "name": "厄立特里亚",
                "value": 15001.072
            },
            {
                "name": "爱沙尼亚",
                "value": 78075.705
            },
            {
                "name": "埃塞俄比亚",
                "value": 5741.159
            },
            {
                "name": "福克兰群岛",
                "value": 46182.038
            },
            {
                "name": "斐济",
                "value": 1298.533
            },
            {
                "name": "芬兰",
                "value": 87095.281
            },
            {
                "name": "法国",
                "value": 5367.693
            },
            {
                "name": "法属圭亚那",
                "value": 860.559
            },
            {
                "name": "法属南部领地",
                "value": 49.581
            },
            {
                "name": "加蓬",
                "value": 63230.866
            },
            {
                "name": "冈比亚",
                "value": 1556.222
            },
            {
                "name": "德国",
                "value": 62066.35
            },
            {
                "name": "佐治亚州",
                "value": 4388.674
            },
            {
                "name": "加纳",
                "value": 24262.901
            },
            {
                "name": "希腊",
                "value": 10876.033
            },
            {
                "name": "格陵兰",
                "value": 1680.64
            },
            {
                "name": "危地马拉",
                "value": 10876.033
            },
            {
                "name": "几内亚",
                "value": 696.167
            },
            {
                "name": "几内亚比绍",
                "value": 11109.999
            },
            {
                "name": "圭亚那",
                "value": 56.546
            },
            {
                "name": "海地",
                "value": 14341.576
            },
            {
                "name": "赫德岛和麦克唐纳群岛",
                "value": 4338.027
            },
            {
                "name": "洪都拉斯",
                "value": 231.169
            },
            {
                "name": "匈牙利",
                "value": 786.126
            },
            {
                "name": "冰岛",
                "value": 7621.204
            },
            {
                "name": "印度",
                "value": 4338.027
            },
            {
                "name": "印度尼西亚",
                "value": 9896.4
            },
            {
                "name": "伊朗",
                "value": 10014.633
            },
            {
                "name": "伊拉克",
                "value": 240676.485
            },
            {
                "name": "爱尔兰",
                "value": 15624.648
            },
            {
                "name": "以色列",
                "value": 4467.561
            },
            {
                "name": "意大利",
                "value": 240676.485
            },
            {
                "name": "象牙海岸",
                "value": 30962.38
            },
            {
                "name": "牙买加",
                "value": 318.042
            },
            {
                "name": "日本",
                "value": 7420.368
            },
            {
                "name": "乔丹",
                "value": 60508.978
            },
            {
                "name": "克什米尔",
                "value": 15921.485
            },
            {
                "name": "哈萨克斯坦",
                "value": 2741.485
            },
            {
                "name": "肯尼亚",
                "value": 6454.554
            },
            {
                "name": "科索沃",
                "value": 127352.833
            },
            {
                "name": "科威特",
                "value": 15921.127
            },
            {
                "name": "吉尔吉斯斯坦",
                "value": 40909.194
            },
            {
                "name": "老挝",
                "value": 5334.223
            },
            {
                "name": "老挝人民民主共和国",
                "value": 127352.833
            },
            {
                "name": "拉脱维亚",
                "value": 14364.931
            },
            {
                "name": "黎巴嫩",
                "value": 51452.352
            },
            {
                "name": "莱索托",
                "value": 97.743
            },
            {
                "name": "利比里亚",
                "value": 2991.58
            },
            {
                "name": "利比亚",
                "value": 6395.713
            },
            {
                "name": "立陶宛",
                "value": 4341.092
            },
            {
                "name": "卢森堡",
                "value": 3957.99
            },
            {
                "name": "马达加斯加",
                "value": 6040.612
            },
            {
                "name": "马其顿",
                "value": 20758.779
            },
            {
                "name": "马拉维",
                "value": 2008.921
            },
            {
                "name": "马来西亚",
                "value": 3068.457
            },
            {
                "name": "马里",
                "value": 507.885
            },
            {
                "name": "毛里塔尼亚",
                "value": 2090.519
            },
            {
                "name": "墨西哥",
                "value": 31642.36
            },
            {
                "name": "摩尔多瓦",
                "value": 103.619
            },
            {
                "name": "蒙古",
                "value": 21079.532
            },
            {
                "name": "黑山",
                "value": 117886.404
            },
            {
                "name": "摩洛哥",
                "value": 507.885
            },
            {
                "name": "莫桑比克",
                "value": 13985.961
            },
            {
                "name": "缅甸",
                "value": 51931.231
            },
            {
                "name": "纳米比亚",
                "value": 620.078
            },
            {
                "name": "荷兰",
                "value": 2712.738
            },
            {
                "name": "新喀里多尼亚",
                "value": 23967.265
            },
            {
                "name": "新西兰",
                "value": 3609.42
            },
            {
                "name": "尼泊尔",
                "value": 15013.694
            },
            {
                "name": "尼加拉瓜",
                "value": 28275.835
            },
            {
                "name": "尼日尔",
                "value": 2178.967
            },
            {
                "name": "尼日利亚",
                "value": 246.379
            },
            {
                "name": "朝鲜",
                "value": 15893.746
            },
            {
                "name": "北塞浦路斯",
                "value": 159707.78
            },
            {
                "name": "挪威",
                "value": 5822.209
            },
            {
                "name": "阿曼",
                "value": 16615.243
            },
            {
                "name": "巴基斯坦",
                "value": 4891.251
            },
            {
                "name": "巴拿马",
                "value": 26846.016
            },
            {
                "name": "巴布亚新几内亚",
                "value": 4368.136
            },
            {
                "name": "巴拉圭",
                "value": 2802.768
            },
            {
                "name": "秘鲁",
                "value": 173149.306
            },
            {
                "name": "刚果共和国",
                "value": 3678.128
            },
            {
                "name": "菲律宾",
                "value": 29262.83
            },
            {
                "name": "波兰",
                "value": 93444.322
            },
            {
                "name": "葡萄牙",
                "value": 6858.945
            },
            {
                "name": "波多黎各",
                "value": 38198.754
            },
            {
                "name": "卡塔尔",
                "value": 3709.671
            },
            {
                "name": "塞尔维亚共和国",
                "value": 1.468
            },
            {
                "name": "罗马尼亚",
                "value": 10589.792
            },
            {
                "name": "俄罗斯",
                "value": 6459.721
            },
            {
                "name": "卢旺达",
                "value": 1749.713
            },
            {
                "name": "萨摩亚",
                "value": 11749.713
            },
            {
                "name": "沙特阿拉伯",
                "value": 21861.476
            },
            {
                "name": "塞内加尔",
                "value": 21861.476
            },
            {
                "name": "塞尔维亚",
                "value": 18862.257
            },
            {
                "name": "塞拉利昂",
                "value": 10836.732
            },
            {
                "name": "斯洛伐克",
                "value": 514.648
            },
            {
                "name": "斯洛文尼亚",
                "value": 27258.387
            },
            {
                "name": "所罗门群岛",
                "value": 35652.002
            },
            {
                "name": "索马里兰",
                "value": 9940.929
            },
            {
                "name": "索马里",
                "value": 12950.564
            },
            {
                "name": "南非",
                "value": 526.447
            },
            {
                "name": "南乔治亚和南桑德威奇群岛",
                "value": 6218.195
            },
            {
                "name": "韩国",
                "value": 5751.976
            },
            {
                "name": "南苏丹",
                "value": 6218.195
            },
            {
                "name": "西班牙",
                "value": 9636.173
            },
            {
                "name": "斯里兰卡",
                "value": 9636.173
            },
            {
                "name": "苏丹",
                "value": 3573.024
            },
            {
                "name": "苏里南",
                "value": 524.96
            },
            {
                "name": "斯威士兰",
                "value": 5433.437
            },
            {
                "name": "瑞典",
                "value": 2054.232
            },
            {
                "name": "瑞士",
                "value": 9382.297
            },
            {
                "name": "叙利亚",
                "value": 1193.148
            },
            {
                "name": "塔吉克斯坦",
                "value": 7830.534
            },
            {
                "name": "坦桑尼亚",
                "value": 9876.785
            },
            {
                "name": "泰国",
                "value": 11720.781
            },
            {
                "name": "巴哈马",
                "value": 6306.014
            },
            {
                "name": "多哥",
                "value": 66402.316
            },
            {
                "name": "特立尼达和多巴哥",
                "value": 7627.326
            },
            {
                "name": "突尼斯",
                "value": 5041.995
            },
            {
                "name": "土耳其",
                "value": 10016.797
            },
            {
                "name": "土库曼斯坦",
                "value": 1328.095
            },
            {
                "name": "乌干达",
                "value": 10631.83
            },
            {
                "name": "乌克兰",
                "value": 72137.546
            },
            {
                "name": "阿拉伯联合酋长国",
                "value": 44973.33
            },
            {
                "name": "大不列颠联合王国",
                "value": 33987.213
            },
            {
                "name": "坦桑尼亚联合共和国",
                "value": 46050.22
            },
            {
                "name": "美国",
                "value": 3371.982
            },
            {
                "name": "美利坚合众国",
                "value": 312247.116
            },
            {
                "name": "乌拉圭",
                "value": 27769.27
            },
            {
                "name": "乌兹别克斯坦",
                "value": 236.299
            },
            {
                "name": "瓦努阿图",
                "value": 89047.397
            },
            {
                "name": "委内瑞拉",
                "value": 236.299
            },
            {
                "name": "越南",
                "value": 13.565
            },
            {
                "name": "西岸",
                "value": 22763.008
            },
            {
                "name": "西撒哈拉",
                "value": 51452.352
            },
            {
                "name": "也门",
                "value": 13216.985
            },
            {
                "name": "赞比亚",
                "value": 13076.978
            },
            {
                "name": "津巴布韦",
                "value": 11056.426
            }
        ]
    }

    return response


@app.route('/api/count')
def get_count():
    consumer = KafkaConsumer('history', bootstrap_servers=['188.131.179.244:9092'])
    i = 0
    for msg in consumer:
        result = ((msg.value).decode('utf8')).replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        i += 1
        if i > 0 and msg is not None and result != "":
            break
    resList = []
    returnList = []
    resList = result.split(", ")
    for item in resList:
        temp_dict = {}
        temp_list = item.split(": ")
        temp_dict['word'] = temp_list[0][1:-1]
        temp_dict['count'] = int(temp_list[1])
        returnList.append(temp_dict)
        returnJson = json.dumps(returnList)
    return returnJson


if __name__ == '__main__':
    app.run()
