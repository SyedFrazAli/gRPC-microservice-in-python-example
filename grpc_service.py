
from concurrent import futures
import grpc
import auth_pb2
import auth_pb2_grpc


class AuthServiceImpl(auth_pb2_grpc.AuthServiceServicer):
    def AuthenticateUser(self, request, context):
        # Simplified authentication logic
        if request.username == "user" and request.password == "pass":
            return auth_pb2.AuthResponse(success=True, message="Authentication successful")
        else:
            return auth_pb2.AuthResponse(success=False, message="Authentication failed")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
