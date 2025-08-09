```sh
docker build -t mygrpc .
docker images
docker run -d -p 50051:50051 --name mygrpc -v .:/root mygrpc sh -c "/root/server/build/server"
docker logs -f mygrpc
```