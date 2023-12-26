import trimesh
from trimesh.proximity import ProximityQuery
import numpy as np 
import networkx as nx 

class Router:
    def __init__(self) -> None:
        """  """
        pass 



    def euclidean_path(self, origin, destination):
        """
        origin point: [x, y, z] 
        destination point: [x, y, z]
        """
        path = [origin, destination] 
        return path 


    def shortest_distance_path(self, mesh, origin, destination):
        """
        Get origin and destination coordinates 
        Find closest mesh vertices to each 
        Path from those 
        Return path coordinates
        """        
        path_coordinates = []  

        # Find closest mesh vertices for origin and destination points 
        meshQuery = ProximityQuery(mesh)
        distances, vertex_ids = meshQuery.vertex([origin, destination]) 
        
        edges = mesh.edges_unique 
        length = mesh.edges_unique_length 

        g = nx.Graph()
        for edge, L in zip(edges, length):
            g.add_edge(*edge, length=L)

        # start_vertex = 0
        # end_vertex = int(len(mesh.vertices) / 2.0)

        path = nx.shortest_path(g,
                                source=vertex_ids[0],
                                target=vertex_ids[-1],
                                weight='length')   
              
        # Convert path to coordinates 
        # 1. Convert indices to coordinates
        for vertice_index in path: 
            path_coordinates.append(list(mesh.vertices[vertice_index])) 
            # print(mesh.vertices[vertice_index])

        # 2. Apply global transform 
            
        return path_coordinates
    

if __name__ == "__main__":
    mesh = trimesh.load_mesh('/Users/nathan/github/conformal_designer/flask_server/static/models/wing/wing.stl') 
    router = Router() 
    path = router.shortest_distance_path(mesh, [0,0,0], [30,30,30]) 

    print(path) 