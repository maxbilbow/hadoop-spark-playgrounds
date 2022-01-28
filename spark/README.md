```shell
docker build -f Dockerfile -t spark-play .
docker tag spark-play:latest spark-play:staging

docker run -p 4040:4040 -p 6066:6066 -p 7077:7077 -v `pwd`/workspace:/workspace --name spark-playground <image_tag> 

docker exec -it spark-playground /bin/bash
```