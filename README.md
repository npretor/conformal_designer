# Conformal Circuit Designer
This is a conformal PCB designer that uses ThreeJS for the modeling and frontend, and python on the backend for file parsing and routing on a mesh. 
![alt text](/media/debug_screenshot.png)

## Installation 
```
./install.sh 
```
## Build 
For deployment platform MUST BE BUILT FOR AMD64 for the server 
```
docker build --platform linux/amd64 -t flask-container .
```

## Run
```
docker run -it -p 8000:8000 flask-container:latest
```

## Deploy 

1. Push the container to AWS 
```
aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container
```

2. Start the service 
```
aws lightsail create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json
```

## Local testing 

Build the server 
```
docker build -t flask-container .
docker run -it -p 8000:8000 flask-container:latest
```

Run in the container 
```
source venv/bin/activate 
cd flask_server
python3 app.py 
```

