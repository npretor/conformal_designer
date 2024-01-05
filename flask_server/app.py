import os, io
import json 
from flask import Flask, render_template, request, redirect, jsonify, Response, send_file
import trimesh

import sys 
sys.path.append('..') 
from Spatial import Router 
from MeshParser import MeshParser


app = Flask(__name__)


# - - - - - - - - Initialize the database - - - - - - - - # 
database = {}
database["smd_components"]  = {}
database["components_cache"]  = {}
database["active_component_id"] = None 
database['smd_components']['0402'] = [0.5, 0.35, 1.0] # Width, height, depth 
database['smd_components']['0603'] = [0.85, 0.45, 1.550] # Width, height, depth  

# - - - - - - - - Load the primary 3D model - - - - - - - - # 
mesh_path = './static/models/wing/wing.stl'
mesh_parser = MeshParser() 
mesh = mesh_parser.read(mesh_path, preprocess=True) 
mesh_attributes = mesh_parser.getAttributesJSON(mesh) 


# - - - - - - - - Initialize the router - - - - - - - - # 
router = Router() 


# - - - - - - - - Routes - - - - - - - - # 
@app.route("/")
def home():

    return render_template('index.html', mesh_attributes=mesh_attributes, my_components=database['smd_components']) 

@app.route("/primary_mesh_file", methods={"GET"}) 
def primary_mesh_file():
    f = mesh_parser.export(mesh)
    # import ipdb; ipdb.set_trace()
    return send_file(io.BytesIO(f), mimetype='application/sla') 

@app.route("/save_components", methods={"GET","POST"})
def save_components():

    database["components_cache"] = json.loads(request.data) 

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@app.route("/place", methods={"GET", "POST"}) 
def place():
    """
    This assumes everything is a variant of box-geometry 
    Returns     
        Component shape: (width, height, depth) 
    """

@app.route("/set_active_component", methods={"GET", "POST"}) 
def set_active_component():
    if request.method == 'POST':
        component_id = json.loads(request.data)['active_component_id']
        print("Active component: ",component_id) 
        
        database["active_component_id"] = component_id
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    else:
        component_id = database["active_component_id"] 
        active_component_shape = database['smd_components'][str(component_id)] 
        print('active component id is: ', component_id) 
        print("shape is: ", active_component_shape)

        return jsonify(active_component_shape) 

@app.route("/list_components", methods={"GET", "POST"}) 
def list_components():
    """
    0402 = 0.04in long x 0.02in wide x 0.02in tall  
    
    """
    my_components = {} 
    my_components['0402'] = [0.5, 0.35, 1.0] # Width, height, depth 
    my_components['0603'] = [0.85, 0.45, 1.550] # Width, height, depth 
    return jsonify(my_components) 


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
