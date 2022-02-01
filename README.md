## Prerequisites

Install [Docker](https://docker.com/get-started)

## Getting Started

1. Download this repo, open a terminal, and navigate to its location. 

2.  Build and run the containers
```shell
docker-compose up -d
```
3. Check everything is ready:
```shell
docker ps # should show hadoop-playground and spark-playground up and running
```
## Access Hadoop
```shell
docker exec -it hadoop-playground /bin/bash
```


## Access Spark
```shell
docker exec -it spark-playground /bin/bash
```

## Access Jupyter Notebook

1. Connect to the container:
```shell
docker exec -it jupyter-playground /bin/bash
```

2. Copy the server token:
```shell
jupyter server list
# Prints something like:
# http://a0542f50464f:8888/?token=d48af4be9f9c9ccc9226d2b69f689374097f1f26244b8f71
```

3. Copy the token and load in your browser [localhost:8888/?token=d48af...]()
## Cleaning Up
```shell
docker-compose down # Stop and remove containers
```
