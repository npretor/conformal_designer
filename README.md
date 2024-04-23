# Conformal Circuit Designer
This is a conformal PCB designer that uses ThreeJS for the modeling and frontend, and python on the backend for file parsing and routing on a mesh. 

## Installation 
```
./install.sh 
```



### Build for deploy - MUST BE BUILT FOR AMD64 for the server 
```
docker build --platform linux/amd64 -t flask-container .
```

### Build for local testing 
```
docker build -t flask-container .
```

## Docker run  
```
docker run -it flask-container:latest
```

## Push the container to AWS 
```
aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container

```

> Modify the containers.json if needed 

## Deploy 
```
aws lightsail create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json
```

## Startup 
```
source venv/bin/activate 
cd flask_server
python3 app.py 
```

