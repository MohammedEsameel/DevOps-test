# DevOps-Test
This is a simple helm chart for personal usage 
I will assume that you have installed the following tools
- Helm 3.7
- Minikube v1.23.2 
- Docker ce

This Project contains simple Pyhton application exposed by Flask , you can use GET http request then you will receive some random json data

----------------------------------------------------------------------------------------------------------------------
## Installation
You need to pull the Docker container image of that application from Docker hub
```
docker pull mohammedismel/devops-test:latest
```
After pulling the image from docker hub, check the image name 
```
docker images
```
You should see this content 
```
REPOSITORY                                         TAG               IMAGE ID       CREATED          SIZE    
mohammedismel/devops-test                          latest            f6c7eb1e7b3d   29 minutes ago   191MB   
python                                             3.8-slim-buster   514a7722ffa9   3 days ago       114MB         
```
----------------------------------------------------------------------------------------------------------------------
## Testing 
You need to download the project
```
git clone https://github.com/MohammedEsameel/DevOps-test.git
```
Check the container by installing this tool
```
curl -LO https://storage.googleapis.com/container-structure-test/latest/container-structure-test-linux-amd64 && chmod +x container-structure-test-linux-amd64 && sudo mv container-structure-test-linux-amd64 /usr/local/bin/container-structure-test
```
Then i prepared  a simple test.yaml file 
```
container-structure-test test --image mohammedismel/devops-test:latest --config DevOps-test/app/test.yaml
```

----------------------------------------------------------------------------------------------------------------------
## Deploy in Kube Cluster
Install the chart using helm commands
```
helm install myfirstapp DevOps-test
```
You will see this message 
```
NAME: myfirstapp
LAST DEPLOYED: Sat Oct  9 21:32:43 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  http://myapp.net/
```

----------------------------------------------------------------------------------------------------------------------
## Get the Results
Now you should check the IP address that will be assigned by nginx ingress using this line 
```
kube get ing
```
First you will see the IP address empty like the message below
```
NAME   CLASS   HOSTS       ADDRESS   PORTS   AGE
api    nginx   myapp.net             80      49s
```
If you still don't see the IP address you should check if ingress is enabled in minikube , by defualt it is disabled , you should enable ingress controller Pod by using this command 
```
minikube addons enable ingress
```
Wait a while then you will see the address assigned
```
NAME   CLASS   HOSTS       ADDRESS        PORTS   AGE
api    nginx   myapp.net   192.168.49.2   80      7m
```
Now you should add the domain name to the hosts file in your system
```
vim /etc/hosts
```
And add this line 
```
192.168.49.2 myapp.net
```
To check the application API type this lines
```
curl  http://myapp.net/
```
You will get these results , that generated by the faker inside the API 
```
{
  "address": "4848 Smith Overpass Apt. 864\nEast Joseph, MS 02831", 
  "created_at": "2009", 
  "name": "Teresa Edwards"
}
```
To check the application Mertics 
```
curl  http://myapp.net/metrics
```
you will see Metrics
```
python_gc_objects_collected_total{generation="0"} 333.0
python_gc_objects_collected_total{generation="1"} 63.0
python_gc_objects_collected_total{generation="2"} 0.0
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
python_gc_collections_total{generation="0"} 88.0
python_gc_collections_total{generation="1"} 7.0
python_gc_collections_total{generation="2"} 0.0
```
Check your helm chart information by typing 
```
helm list
```
You will see
```
NAME      	NAMESPACE	REVISION	UPDATED                               	STATUS  	CHART           	APP VERSION
myfirstapp	default  	1       	2021-10-09 21:32:43.34866459 +0300 +03	deployed	test-chart-0.1.0	1.16.0     
```
----------------------------------------------------------------------------------------------------------------------
## Tshoot
If you face some issues with Minikube image pulling you just type this command 
```
eval $(minikube -p minikube docker-env)
```
- Then pull the image for local docker repositry again and then install the helm chart.
----------------------------------------------------------------------------------------------------------------------
## Notice 
You will find OPA example , i just put it with this project to Mark it in TODO list
### TODO list
- Helm Testing
- Helm Hooks
- OPA
