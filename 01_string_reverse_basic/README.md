# gRPC C++ Get Started Example

[medium-guide]: https://medium.com/%40shradhasehgal/get-started-with-grpc-in-c-36f1f39367f4
[code-repo]: https://github.com/shradhasehgal/grpc/tree/master
[grpc-quickstart]: https://grpc.io/docs/languages/cpp/quickstart/

This project is based on the guide ["Get started with gRPC in C++" by Shradha Sehgal][medium-guide] and its [original code repository][code-repo].

It demonstrates how to:
- Define a service in a `.proto` file
- Use the protobuf compiler to generate server and client code
- Write a simple string reversal server and client using the C++ gRPC API

For official instructions and more examples, see the [gRPC C++ Quick Start][grpc-quickstart].

## Installation

**Linux example:**
```sh
sudo apt install -y cmake
sudo apt install -y build-essential autoconf libtool pkg-config
# Optionally install a newer CMake version if needed
```

**Clone and build gRPC:**
```sh
git clone -b $(curl -L https://grpc.io/release) https://github.com/grpc/grpc
cd grpc
mkdir -p cmake/build
cd cmake/build
cmake -DgRPC_INSTALL=ON ../..
make
make install
```

## Build Instructions

```sh
mkdir -p cmake/build
cd cmake/build
cmake ../..
make
```

## Try it!

**Run the server:**
```sh
./server
Server listening to port localhost 500051
```

**From a different terminal, run the client:**
```sh
./client
Original string: grpc is cool!
Reversed string: !looc si cprg
```

If the server is not running, the client will display an error about failing to connect.