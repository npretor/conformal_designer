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

