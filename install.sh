#!/bin/bash
python3 -m venv venv 
source venv/bin/activate
python3 -m pip install Flask kiutils ipdb numpy-stl "trimesh[default]"
