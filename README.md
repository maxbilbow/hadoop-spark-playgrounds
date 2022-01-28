## Getting Started
1. Install [Docker](https://www.docker.com/get-started)
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

## Cleaning Up
```shell
docker-compose down # Stop and remove containers
```