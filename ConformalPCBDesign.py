"""
### Basics I would need to start a conformal design tool 
* A converter from Kicad. Later:  other formats (maybe altium), 3D support, infer the package 3D shape from the pads land pattern + bounding box + standard height 
    * https://github.com/mvnmgrx/kiutils/blob/master/tests/test_schematic.py
    * 
* Viewer 
    * Flask + ThreeJS 
    * 
* GUI to select a component, and select a location, displaying the footprint. Later: Display possible footprint locations 
* Routing
    * Select nets to route 
    * Snap to nearest pad centroid: Use this for fast searching https://github.com/collinhover/threeoctree
    * Show ratsnest (streight line or geodesic) 
    * Select locations on surface. Later: Show curvature, possible paths 
* Export as a STEP, or 3D DXF. Later: Convert to basic gcode, using the local coordinate 
* Mode selection(placing, routing, move(component, trace), ) 
"""
import os 
import numpy

stl_path = "./flask_server/static/models/wing/wing.stl"

def read_with_numpystl():
    from stl import mesh
    
    your_mesh = None 

    try:
        your_mesh = mesh.Mesh.from_file(stl_path)  
    except:
        print('Could not open file') 
        
    # The mesh normals (calculated automatically)
    print(your_mesh.normals)
    # The mesh vectors
    print(your_mesh.v0, your_mesh.v1, your_mesh.v2) 
    return your_mesh

def read_with_pymesh():
    mesh = pymesh.load_mesh("cube.obj") 


def get_closest_points(mesh_points, points):
    # numpy-stl speed issue with getting only vertices
    #    https://github.com/WoLpH/numpy-stl/issues/34

    import numpy as np
    from sklearn.neighbors import KDTree

    # Get distances and indices of nearest three points to four selected points 
    tree = KDTree(mesh_points, leaf_size=2) 
    dist, ind = tree.query(mesh_points[10:15], k=3) 

mesh = read_with_numpystl()
# Get mesh points from vertices 
mesh_points = numpy.concatenate(mesh.vectors) 

dist, ind = get_closest_points(mesh_points, mesh) 

import ipdb; ipdb.set_trace() 


class KicadConverter:
    def __init__(self) -> None:
        """
        Gets a Kicad file path of components returns a list of component objects 
        - Component objects have pads with a shape 
        """ 
        pass 


class Component:
    """
    Start with dead simple, not inheritance or type categories(QFN, SMD, etc) 
    """
    def __init__(self) -> None:
        pass 


class Router:
    def __init__(self) -> None:
        """  """
        pass 

