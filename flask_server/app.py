import os 
import json 
from flask import Flask, render_template, request, redirect, jsonify, Response

app = Flask(__name__)

database = {}
database["components"]  = {}

@app.route("/")
def home():
    return render_template('index.html') 

@app.route("/save_components", methods={"POST"})
def save_components():

    database["components"] = json.loads(request.data) 

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == "__main__":
    # print(os.listdir('.')) 
    app.run(host='0.0.0.0', port=8000, debug=False)  
