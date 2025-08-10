import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    # Connect to the server at localhost:50051
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.ProcessingServicesStub(channel)

    point = hello_pb2.Point3(x=1.0, y=2.0, z=3.0)

    # Call RPC
    response = stub.computeSum(point)

    print("Sum received from server:", response.value)

if __name__ == '__main__':
    run()
