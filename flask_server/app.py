import os 
from flask import Flask, render_template, request, redirect, jsonify 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html') 

if __name__ == "__main__":
    # print(os.listdir('.')) 
    app.run(host='0.0.0.0', port=8000, debug=False) 