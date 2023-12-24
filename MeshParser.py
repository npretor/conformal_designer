import os 
import numpy as np 
from stl import mesh
from sklearn.neighbors import KDTree 


class MeshParser:
    def __init__(self) -> None:
        pass 


    def read(self, filepath):
        try:
            stl_data = mesh.Mesh.from_file(filepath)  
            
        except:
            print(Exception)         

        return stl_data
            

    def get_vertices(self, mesh):
        # Get mesh points from vertices 
        mesh_points = np.concatenate(mesh.vectors) 
        # dist, ind = get_closest_points(mesh_points, mesh) 
        #  import ipdb; ipdb.set_trace()         


    def get_closest_points(mesh_points, query_points, n_points=1):
        """
        mesh_points:  2D numpy array
        query_points:       2D numpy array 
        n_points: integer of points to return 
        """
        # numpy-stl speed issue with getting only vertices
        #    https://github.com/WoLpH/numpy-stl/issues/34


        # Get distances and indices of nearest three points to four selected points 
        tree = KDTree(mesh_points, leaf_size=2) 
        dist, ind = tree.query(query_points, k=n_points) 
        return 
        