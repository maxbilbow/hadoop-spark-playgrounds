```shell
docker build -f Dockerfile -t <image_tag> .

docker run -v `pwd`/workspace:/workspace --name hadoop-playground <image_tag> 

docker exec -it hadoop-playground /bin/bash
```