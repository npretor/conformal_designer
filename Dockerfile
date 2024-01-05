# Set base image (host OS)
FROM python:3.11

# By default, listen on port 5000
EXPOSE 8000/tcp

# Set the working directory in the container
WORKDIR /flask_server 

# Copy the dependencies file to the working directory
COPY install.sh .

# Copy the flask server files 
COPY flask_server/ .

# Install any dependencies
RUN python -m pip install Flask kiutils numpy-stl  networkx 

# Install scipy dependancies 
RUN apt update \
    && apt upgrade -y \
    && apt autoremove -y \
    && apt install -y \
        gcc \
        build-essential \
        zlib1g-dev \
        wget \
        unzip \
        cmake \
        python3-dev \
        gfortran \
        libblas-dev \
        liblapack-dev \
        libatlas-base-dev \
    && apt clean

RUN python -m pip install  "trimesh[easy]" 

COPY LibraryParsers.py . 
COPY MeshParser.py . 
COPY Spatial.py . 


# Specify the command to run on container start
CMD [ "python", "app.py" ] 