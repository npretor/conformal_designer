import os 
import numpy as np 
import trimesh
from trimesh.remesh import subdivide_to_size
from trimesh.exchange.export import export_mesh
from trimesh.exchange import stl 
# from sklearn.neighbors import KDTree 


class MeshParser:
    def __init__(self) -> None:
        self.meshdata = {}


    def read(self, filepath, preprocess=False):
        
        mesh = trimesh.load_mesh(filepath)   
        
        if preprocess:
            mesh = self.preprocess(mesh) 

        return mesh
        

        

    def write(self, mesh, filepath):
        """Get mesh object, write to a file"""
        pass


    def export(self, mesh):
        """
        Gets a mesh object, returns a file object 
        """
        try:
            return stl.export_stl(mesh) 
        except:
            raise 
        


    def preprocess(self, mesh):
        print('starting size: ',len(mesh.vertices)) 

        # vertices, faces, index = subdivide_to_size(mesh.vertices, mesh.faces, max_edge=1, return_index=True) 
        # import ipdb; ipdb.set_trace()
        vertices, faces = trimesh.remesh.subdivide_loop(mesh.vertices, mesh.faces, iterations=1)
        # vertices, faces = subdivide_to_size(mesh.vertices, mesh.faces, max_edge=1) 
        finer_mesh  = trimesh.Trimesh(vertices=vertices, faces=faces) 
        print('ending size: ',len(finer_mesh.vertices)) 
        return finer_mesh 

    
    def getAttributesJSON(self, mesh):
        
        self.meshdata['volume'] = mesh.volume 
        # self.meshdata['is_convex'] = mesh.is_convex 
        self.meshdata['centroid'] = mesh.centroid  
        self.meshdata['area'] = mesh.area  
        self.meshdata['num_vertices'] = len(mesh.vertices) 

        return self.meshdata

    

    def get_vertices(self, mesh):
        # Get mesh points from vertices 
        mesh_points = np.concatenate(mesh.vectors) 
        # dist, ind = get_closest_points(mesh_points, mesh) 
        #  import ipdb; ipdb.set_trace()         


    # def get_closest_points(mesh_points, query_points, n_points=1):
    #     """
    #     mesh_points:  2D numpy array
    #     query_points:       2D numpy array 
    #     n_points: integer of points to return 
    #     """
    #     # numpy-stl speed issue with getting only vertices
    #     #    https://github.com/WoLpH/numpy-stl/issues/34


    #     # Get distances and indices of nearest three points to four selected points 
    #     tree = KDTree(mesh_points, leaf_size=2) 
    #     dist, ind = tree.query(query_points, k=n_points) 

if __name__ == "__main__":

    example_filepath = '/Users/nathan/github/conformal_designer/flask_server/static/models/wing/wing.stl'
    mp = MeshParser()
    mesh = mp.read(example_filepath, preprocess=True)  
    print(mesh)
