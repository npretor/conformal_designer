FROM ubuntu:latest 
WORKDIR /flask_server
COPY . . 

RUN apt-get update && apt-get -y upgrade 
RUN apt-get -y install \
    libeigen3-dev \
    libgmp-dev \
    libgmpxx4ldbl \
    libmpfr-dev \
    libboost-dev \
    libboost-thread-dev \
    libtbb-dev \
    python3-dev \
    curl \
    cmake \
    build-essential \
    libcgal-dev \
    git 

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
RUN python3 get-pip.py    

RUN git clone https://github.com/PyMesh/PyMesh.git && cd PyMesh 
RUN git submodule update --init 
RUN export PYMESH_PATH=`pwd`
RUN python3 -m pip install Flask kiutils ipdb numpy scipy 
RUN python3 -m pip install -r $PYMESH_PATH/python/requirements.txt 