cmake_minimum_required(VERSION 3.20)

project(myserver)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
find_package(Protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG)

add_executable(server src/server.cc)
target_link_libraries(server gRPC::grpc++)