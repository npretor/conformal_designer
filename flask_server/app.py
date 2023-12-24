import os 
import json 
from flask import Flask, render_template, request, redirect, jsonify, Response

app = Flask(__name__)


# - - - - - - - - Initialize the database - - - - - - - - # 
database = {}
database["components"]  = {}


# - - - - - - - - Load the primary 3D model - - - - - - - - # 
primary_stl_path = "./flask_server/static/models/wing/wing.stl" 

@app.route("/")
def home():
    return render_template('index.html') 

@app.route("/save_components", methods={"GET","POST"})
def save_components():

    database["components"] = json.loads(request.data) 

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/route",methods={"GET","POST"}) 
def route():
    """
    Get a start and end position 
    Reply with a route 
    """
    response_json = json.loads(request.data)
    # print("response: ", response_json) 

    point1 = {
        "x": response_json["origin"]["x"],
        "y": response_json["origin"]["y"],
        "z": response_json["origin"]["z"]
        }
    point2 = {
        "x": response_json["destination"]["x"],
        "y": response_json["destination"]["y"],
        "z": response_json["destination"]["z"]  
    }

    # print(point1, point2) 
    return jsonify({'success':True, "path":[point1, point2]}) 
    # return json.dumps({'success':True, "path":[point1, point2]}), 200, {'ContentType':'application/json'} 
    #return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == "__main__":
    # print(os.listdir('.')) 
    app.run(host='0.0.0.0', port=8000, debug=False)  
