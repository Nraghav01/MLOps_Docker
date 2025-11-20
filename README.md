# MLOps_Docker
Beginners in Containers, Docker and Docker hub

## Docker Test

docker pull hello-world

docker run hello-world


```bash
docker ps                                   # See a list of all running containers
docker ps -a                                # See a list of all containers, even the ones not running
docker rm <container id>                    # Remove the specified container from this machine
docker rm $(docker ps -a -q)                # Remove all containers from this machine
docker images -a                            # Show all images on this machine (Already executed ones as well)
docker run <image name>                     # To run a docker imager and create a container in local docker desktop
docker rmi <image name>                     # Remove the specified image from this machine
docker rmi $(docker images -q)              # Remove all images from this machine
```

## Launching EC2 instance with Ubntu

### Update cmd

sudo apt-get update -y

sudo apt-get upgrade


### Docker install
```bash
curl -fsSL https://get.docker.com -o get-docker.sh    #To install Docker in the ubntu machine

sudo sh get-docker.sh                                 #To unpack the sh docker package in ubntu EC2 instance

sudo usermod -aG docker ubuntu                        #

newgrp docker                                         
```

## Docker Custom image

docker build -t entbappy/mycalapp:latest .

docker run -p 8080:8080 entbappy/mycalapp:latest

docker run -d -p 8080:8080 entbappy/mycalapp:latest 



## Push to Docker Hub:

1. docker login  
2. docker push entbappy/mycalapp:latest     