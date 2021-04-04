# Como criar o ambiente de docker com gdal

```
docker build t satelitesv1 .

docker run -p 8080:8080 -p 8888:8888 -it satelitesv1

docker ps # veja qual o container ID

docker logs container_id
```