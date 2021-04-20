import logging
import grpc
from concurrent import futures

# proto stub
import grpc_pb2
import grpc_pb2_grpc


def get_logger():
    __logger = logging.getLogger('logger')
    stream_handler = logging.StreamHandler()
    __logger.addHandler(stream_handler)
    __logger.setLevel(logging.DEBUG)
    return __logger


class GrpcService(grpc_pb2_grpc.GrpcServiceServicer):

    def getOne(self, request, context):
        get_logger().debug(request)
        return grpc_pb2.Response(value=[1.1, 2.2, 3.3])

    def serverStream(self, request, context):
        get_logger().debug(request)
        for i in range(1, 4):
            yield grpc_pb2.Response(value=[1.1 * i, 2.2 * i, 3.3 * i])

    def clientStream(self, request_iterator, context):
        for req in request_iterator:
            get_logger().debug(req)
        return grpc_pb2.Response(value=[1.1, 2.2, 3.3])

    def biStream(self, request_iterator, context):
        for req in request_iterator:
            get_logger().debug(req)
            for i in range(1, 4):
                yield grpc_pb2.Response(value=[1.1 * i, 2.2 * i, 3.3 * i])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_GrpcServiceServicer_to_server(GrpcService(), server)
    server.add_insecure_port('[::]:8888')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
