# DevOps-test
This is Simple Helm chart for personal uasage 
I will assume that u have installed helm 3.7 , Minikube v1.23.2 , docker ce

This Project contains simple Pyhton application exposed by flask , you can use get http request the you will gain some fake json data


Stage 1
*you need to download the project
```
git clone https://github.com/MohammedEsameel/DevOps-test.git
cd DevOps-test
```

*build docker image

```
cd DevOps-test/app
docker build . -t api-cat/latest:latest
```
after build type this command 
```
docker images
```
check the containr by installing this tool
curl -LO https://storage.googleapis.com/container-structure-test/latest/container-structure-test-linux-amd64 && chmod +x container-structure-test-linux-amd64 && sudo mv container-structure-test-linux-amd64 /usr/local/bin/container-structure-test

then i prepare simple test.yaml file 
```
container-structure-test test --image api-cat/latest:latest --config test.yaml
```

you should see this content 

REPOSITORY                    TAG               IMAGE ID       CREATED        SIZE
api-cat/latest                latest            dd7e9af55f5e   21 hours ago   190MB
python                        3.8-slim-buster   514a7722ffa9   2 days ago     114MB



stage 2 build the chart using helm commands
```
helm install myfirstapp DevOps-test

```
check your helm chart by typing 

helm list

you will see 

NAME      	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART           	APP VERSION
myfirstapp	default  	6       	2021-10-08 20:40:23.525931395 +0300 +03	deployed	test-chart-0.1.0	1.16.0     











Some basic Git commands are:
```
git status
git add
git commit
```
