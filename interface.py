import streamlit as st
import grpc
import auth_pb2
import auth_pb2_grpc

def authenticate_user(username, password):
    channel = grpc.insecure_channel('localhost:50051')
    stub = auth_pb2_grpc.AuthServiceStub(channel)
    request = auth_pb2.UserCredentials(username=username, password=password)
    response = stub.AuthenticateUser(request)
    return response
st.title("4 : gRPC")
st.title("gRPC Authentication by Fraz")

username = st.text_input("Username:")
password = st.text_input("Password:", type="password")

if st.button("Authenticate"):
    response = authenticate_user(username, password)
    if response.success:
        st.success(response.message)
    else:
        st.error(response.message)
