# Como criar o ambiente de docker com gdal

```
docker build -t satelitesv1 .

docker volume create data

docker run -p 8888:8888 -it -d --mount source=data,destination=/home --name satelites satelitesv1 

docker logs satelites
```

Use a URL da ultima linha do log:

```
[C 2021-04-04 21:56:20.741 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/jpserver-1-open.html
    Or copy and paste one of these URLs:
        http://8bf805c2b4c0:8888/lab?token=881b644c594b39d604917b21e6d8f5e620d46dc723ea8950
     or http://127.0.0.1:8888/lab?token=881b644c594b39d604917b21e6d8f5e620d46dc723ea8950
```