FROM python:3.8
WORKDIR .
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location_event.proto
ENV KAFKA_URL =  kafka-service:9092
ENV KAFKA_TOPIC = test
EXPOSE 5005
ENTRYPOINT ["python", "grpcserver.py"]
