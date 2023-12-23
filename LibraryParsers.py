import os 
import kiutils 
from kiutils.footprint import Footprint 


class KicadConverter:
    def __init__(self) -> None:
        """
        Gets a Kicad file path of components returns a list of component objects in the format ThreeJS needs 
        - Component objects have pads with a shape
        - Ignore 3D geometry and derive from the pads for now 
        """ 
        # eagle_libraries = "/Users/nathan/github/conformal_designer/flask_server/static/ecad/eagle/SparkFun-Eagle-Libraries" 
        # example_library_path = os.path.join(eagle_libraries, "SparkFun-Resistors.lbr") 

    def read(self, path):
        try:
            footprint = Footprint().from_file(path) 
            return footprint
        except:
            raise

    def parse_to_json(self, footprint):
        component = {
            "name": footprint.entryName, 
            # "description": footprint.description, 
            "pads": {}
        }

        # Fill out pad data 
        for i, pad in enumerate(footprint.pads):
            if pad.position.angle == None:
                pad.position.angle = 0 

            component["pads"][i] = {
                "position": (pad.position.X, pad.position.Y),
                "angle": pad.position.angle, 
                "size": (pad.size.X, pad.size.Y) 
            }         
        
        return component 


if __name__ == "__main__":
    kicad_libraries = "/Users/nathan/github/conformal_designer/flask_server/static/ecad/kicad/kicad-footprints/LED_SMD.pretty/"
    component_name = "LED_0201_0603Metric.kicad_mod"
    example_component =  os.path.join(kicad_libraries, component_name) 
    k = KicadConverter() 
    fp = k.read(example_component) 
    print(k.parse_to_json(fp))  
    
