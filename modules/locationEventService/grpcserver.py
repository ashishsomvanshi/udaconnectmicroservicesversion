
import grpc
from concurrent import futures
import time
import json
import os
from kafka import KafkaProducer
import location_event_pb2_grpc as pb2_grpc
import location_event_pb2 as pb2

kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]

producer = KafkaProducer(bootstrap_servers=kafka_url)

class EventLocationService(pb2_grpc.EventLocationServiceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        request_value = {
            'userId': int(request.userId),
            'latitude': int(request.latitude),
            'longitude': int(request.longitude)
        }
        user_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(kafka_topic, user_encode_data)
        return pb2.EventLocationMessage(**request_value)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    pb2_grpc.add_EventLocationServiceServicer_to_server(EventLocationService(), server)
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()