import grpc
import location_event_pb2_grpc as pb2_grpc
import location_event_pb2 as pb2

print("Sending Location")

channel = grpc.insecure_channel("localhost:5005")
stub = pb2_grpc.EventLocationServiceStub(channel)

user_location_1 = pb2.EventLocationMessage(
    userId=500,
    latitude=-600,
    longitude=70
)

user_location_2 = pb2.EventLocationMessage(
    userId=300,
    latitude=-200,
    longitude=40
)

response_1 = stub.Create(user_location_1)
response_2 = stub.Create(user_location_2)

print("Sent User Locations")
print(user_location_1, user_location_2)
