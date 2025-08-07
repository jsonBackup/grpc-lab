# gRPC C++ Async Hello World Example

You can find a complete set of instructions for building gRPC and running the
Hello World app in the [C++ Quick Start][].

## Build Instructions

```sh
mkdir -p cmake/build
pushd cmake/build
cmake -DCMAKE_PREFIX_PATH=$MY_INSTALL_DIR ../..
make -j 4
```

## Try it!

Run the example from the build directory (`cmake/build`):

**Run the async server:**
```sh
./greeter_async_server
Server listening on 0.0.0.0:50051
```

**From a different terminal, run the async client and see the client output:**
```sh
./greeter_async_client
Greeter received: Hello world
```

[C++ Quick Start]: https://grpc.io/docs/languages/cpp/quickstart
