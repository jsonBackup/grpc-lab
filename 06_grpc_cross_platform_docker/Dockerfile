FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    git

WORKDIR /deps

RUN git clone --recurse-submodules -b v1.74.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc

RUN mkdir -p /deps/grpc/build && cd /deps/grpc/build && cmake -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF .. && make -j8 install
