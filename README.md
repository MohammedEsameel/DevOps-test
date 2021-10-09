# DevOps-test
This is Simple Helm chart for personal uasage 
I will assume that u have installed helm 3.7 , Minikube v1.23.2 , docker ce

This Project contains simple Pyhton application exposed by flask , you can use get http request the you will gain some fake json data

first you need to pull the docker container image of that application from docker hum

```
docker pull mohammedismel/devops-test:latest
```
after pull the image from docker hub, check the image name 
```
docker images
```
you should see this content 

REPOSITORY                                         TAG               IMAGE ID       CREATED          SIZE
mohammedismel/devops-test                          latest            f6c7eb1e7b3d   29 minutes ago   191MB
python                                             3.8-slim-buster   514a7722ffa9   3 days ago       114MB          

check the containr by installing this tool
```
curl -LO https://storage.googleapis.com/container-structure-test/latest/container-structure-test-linux-amd64 && chmod +x container-structure-test-linux-amd64 && sudo mv container-structure-test-linux-amd64 /usr/local/bin/container-structure-test
```
then i prepare simple test.yaml file 
```
container-structure-test test --image mohammedismel/devops-test:latest --config DevOps-test/app/test.yaml
```

Stage 1
*you need to download the project
```
git clone https://github.com/MohammedEsameel/DevOps-test.git
```
stage 2 build the chart using helm commands
```
helm install myfirstapp DevOps-test
```
you will see this message 

NAME: myfirstapp
LAST DEPLOYED: Sat Oct  9 21:32:43 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://myapp.net/

to check the application API type this lines
```
curl  http://myapp.net/
```
you will got this message 

{
  "address": "4848 Smith Overpass Apt. 864\nEast Joseph, MS 02831", 
  "created_at": "2009", 
  "name": "Teresa Edwards"
}


to check the application Mertics 
```
curl  http://myapp.net/metrics
```
you will see Metrics
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 333.0
python_gc_objects_collected_total{generation="1"} 63.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 88.0
python_gc_collections_total{generation="1"} 7.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
---

check your helm chart information by typing 
```
helm list
```
you will see

NAME      	NAMESPACE	REVISION	UPDATED                               	STATUS  	CHART           	APP VERSION
myfirstapp	default  	1       	2021-10-09 21:32:43.34866459 +0300 +03	deployed	test-chart-0.1.0	1.16.0     



Tshoot
if you face some issues with Minikube image pulling you just type this command 
```
eval $(minikube -p minikube docker-env)
```
then pull the image for local docker repositry again 
and then install the helm chart.

---
Notice you will find OPA example , i just put it with this project to Mark it in TODO list
TODO list
* Helm Testing
* Helm Hooks
* OPA
