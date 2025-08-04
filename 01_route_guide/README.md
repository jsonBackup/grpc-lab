# gRPC Basics: C++ sample code

The files in this folder are the samples used in [gRPC Basics: C++][],
a detailed tutorial for using gRPC in C++.

[gRPC Basics: C++]:https://grpc.io/docs/languages/cpp/basics

## Configuration

The RouteGuide proto definition is available [here](./protos/route_guide.proto).
The server takes the following command-line argument -
* db_path - Path to json file containing database. Defaults to `examples/cpp/route_guide/route_guide_db.json` on bazel builds, and `../../route_guide_db.json` for non-bazel builds.

## Build Instructions

```sh
mkdir -p cmake/build
pushd cmake/build
cmake -DCMAKE_PREFIX_PATH=$MY_INSTALL_DIR ../..
make -j 4
```

## Running the example

To run the server -

```sh
./route_guide_server
Server listening on 0.0.0.0:50051
```

To run the client -

```sh
./route_guide_client
-------------- GetFeature --------------
Found feature called Berkshire Valley Management Area Trail, Jefferson, NJ, USA at 40.9146, -74.6189
Found no feature at 0, 0
-------------- ListFeatures --------------
Looking for features between 40, -75 and 42, -73
Found feature called Patriots Path, Mendham, NJ 07945, USA at 40.7838, -74.6144
Found feature called 101 New Jersey 10, Whippany, NJ 07981, USA at 40.8123, -74.3999
Found feature called U.S. 6, Shohola, PA 18458, USA at 41.3628, -74.9016
Found feature called 5 Conners Road, Kingston, NY 12401, USA at 42, -74.0371
Found feature called Mid Hudson Psychiatric Center, New Hampton, NY 10958, USA at 41.4008, -74.3951
...
Found feature called 3 Hasta Way, Newton, NJ 07860, USA at 41.0248, -74.7128
ListFeatures rpc succeeded.
-------------- RecordRoute --------------
Visiting point 40.1013, -74.4035
Visiting point 40.0342, -74.8789
Visiting point 40.611, -74.2187
Visiting point 40.5314, -74.9836
Visiting point 41.0322, -74.7872
Visiting point 41.37, -74.2135
Visiting point 40.4227, -74.0517
Visiting point 41.2856, -74.5149
Visiting point 41.8465, -74.6859
Visiting point 40.1827, -74.0294
Finished trip with 10 points
Passed 5 features
Travelled 777288 meters
It took 11 seconds
-------------- RouteChat --------------
Sending message First message at 0, 0
Sending message Second message at 0, 1
Sending message Third message at 1, 0
Sending message Fourth message at 0, 0
Got message First message at 0, 0
```