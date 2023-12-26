import os 
import json 
from flask import Flask, render_template, request, redirect, jsonify, Response
import trimesh

import sys 
sys.path.append('..') 
from Spatial import Router 


app = Flask(__name__)


# - - - - - - - - Initialize the database - - - - - - - - # 
database = {}
database["components"]  = {}


# - - - - - - - - Load the primary 3D model - - - - - - - - # 
primary_stl_path = "./flask_server/static/models/wing/wing.stl" 
mesh = trimesh.load_mesh('/Users/nathan/github/conformal_designer/flask_server/static/models/wing/wing.stl') 


# - - - - - - - - Initialize the router - - - - - - - - # 
router = Router() 


# - - - - - - - - Routes - - - - - - - - # 
@app.route("/")
def home():
    return render_template('index.html') 

@app.route("/save_components", methods={"GET","POST"})
def save_components():

    database["components"] = json.loads(request.data) 

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route("/route_euclidean",methods={"GET","POST"}) 
def route_euclidean():
    """
    Get a start and end position 
    Reply with a route path = [[x,y,z],[x,y,z],...]
    """
    response_json = json.loads(request.data)

    origin      = response_json["origin"] 
    destination = response_json["destination"] 

    path = router.euclidean_path(origin, destination)
    
    return jsonify({'success':True, "path":path}) 


@app.route("/route_shortest_distance",methods={"GET", "POST"})
def route_shortest_distance():

    response_json = json.loads(request.data)
    origin      = response_json["origin"] 
    destination = response_json["destination"] 

    path = router.shortest_distance_path(mesh, origin, destination)
    
    return jsonify({'success':True, "path":path}) 



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)  
