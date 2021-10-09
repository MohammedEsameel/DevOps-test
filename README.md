# DevOps-test
This is Simple Helm chart for personal uasage 
I will assume that u have installed helm 3.7 , Minikube v1.23.2 , docker ce



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
you should see this content 

REPOSITORY                    TAG               IMAGE ID       CREATED        SIZE
api-cat/latest                latest            dd7e9af55f5e   21 hours ago   190MB
python                        3.8-slim-buster   514a7722ffa9   2 days ago     114MB

Some basic Git commands are:
```
git status
git add
git commit
```
