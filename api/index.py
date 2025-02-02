from flask import Flask, request, jsonify

app = Flask(__name__)

# Data to simulate marks
marks_list = [{"name":"d2j7kadV","marks":16},
{"name":"S5esxMzx1","marks":90},
{"name":"TFnxFkcT","marks":88},
{"name":"b7Y3KIVL","marks":42},
{"name":"pqU57WA","marks":16},
{"name":"v0HznIfA7","marks":43},
{"name":"f7stbObhN","marks":87},
{"name":"njxOd","marks":61},
{"name":"g","marks":79},
{"name":"mdcvn","marks":60},
{"name":"mKyNvyPji","marks":38},
{"name":"KiiM","marks":81},
{"name":"NlEzhB","marks":45},
{"name":"kn88","marks":33},
{"name":"0VG5re","marks":82},
{"name":"bQ4rA","marks":77},
{"name":"nI","marks":41},
{"name":"jCf4I","marks":58},
{"name":"mX","marks":54},
{"name":"ANtLk","marks":68},
{"name":"ShM2Ly7","marks":32},
{"name":"0nn7VyepBJ","marks":96},
{"name":"B6uP","marks":87},
{"name":"KqXoa","marks":89},
{"name":"PTHXR0zB","marks":99},
{"name":"5mS","marks":58},{"name":"pXoxU0EU4","marks":3},
{"name":"1yJgZYvbd","marks":34},{"name":"R9CL98","marks":15},
{"name":"VvJMQgj","marks":47},{"name":"893zGP0W","marks":95},{"name":"4AU1ocLN","marks":74},
{"name":"h","marks":76},{"name":"Vhee0s","marks":49},
{"name":"73A9rV","marks":90},{"name":"9EvrG","marks":54},{"name":"TzZjJF","marks":40},{"name":"Dl","marks":18},{"name":"F","marks":4},{"name":"XVrRbHBAVa","marks":30},
{"name":"BtmVfT","marks":73},{"name":"XWIIz1","marks":69},
{"name":"HU1cfIoH","marks":59},{"name":"4","marks":48},{"name":"pCf","marks":69},{"name":"N5xVPculo","marks":26},{"name":"RhlQYY1UBQ","marks":33},{"name":"EJYzB","marks":15},
{"name":"7Tj","marks":52},{"name":"l","marks":36},{"name":"NkxVgmV7","marks":80},{"name":"CbJCFXw","marks":16},{"name":"WrSAHaF3","marks":14},{"name":"u2rzj2","marks":72},
{"name":"t","marks":61},{"name":"lJyZB","marks":8},
{"name":"so","marks":3},{"name":"Y3bkjG7","marks":23},{"name":"OmDSuLHpE","marks":75},{"name":"aIRWCTP","marks":66},{"name":"lqGA","marks":61},
{"name":"GPH","marks":50},{"name":"uR2","marks":4},{"name":"BLK","marks":78},
{"name":"6W0","marks":23},{"name":"p28Yoj","marks":59},{"name":"4ja6dwaupy","marks":84},{"name":"EtOJECQ","marks":20},{"name":"y","marks":50},
{"name":"OZdfrSYw8","marks":12},{"name":"SPH","marks":69},{"name":"dn7JVqxwxz","marks":44},{"name":"Z3MOZuA","marks":36},
{"name":"C","marks":56},{"name":"uv3wB2u93","marks":5},
{"name":"Dsaw6PoGdY","marks":7},{"name":"5L","marks":69},{"name":"tQBEGo","marks":12},
{"name":"fdM","marks":22},{"name":"BMJ","marks":62},{"name":"b","marks":59},{"name":"FqxWlvyM","marks":87},
{"name":"FD00ciQkeG","marks":67},{"name":"1","marks":50},{"name":"ucS1","marks":94},{"name":"Rojle","marks":20},
{"name":"Eunl07","marks":68},{"name":"Uk8a0t","marks":11},{"name":"pRvC","marks":21},{"name":"AN60O6Vy","marks":96},
{"name":"1MO","marks":61},{"name":"RVSS","marks":48},{"name":"SkEkesFBGw","marks":92},{"name":"te","marks":69},
{"name":"L3RLA","marks":20},{"name":"DojdEa","marks":27},{"name":"wSwH","marks":31},{"name":"gBLXFkqoMo","marks":94},{"name":"ZaUrgTgPj","marks":81},{"name":"VqUMSl","marks":75}]

# Helper function to find marks by name
def find_marks(name):
    for entry in marks_list:
        if entry["name"] == name:
            return entry["marks"]
    return 0  # Default if name is not found

@app.route('/api', methods=['GET'])
def get_marks():
    # Extract 'name' parameters from query string
    names = request.args.getlist('name')

    # Find marks for each name
    marks = [find_marks(name) for name in names]

    # Enable CORS by adding the necessary headers
    response = jsonify({"marks": marks})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
