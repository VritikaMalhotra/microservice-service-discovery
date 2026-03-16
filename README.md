# Microservice Service Discovery Project

This project demonstrates service discovery using a service registry (Consul).

## Architecture

Client → Consul → Service Instances

Two service instances register themselves with Consul.  
The client queries Consul to discover available instances and randomly calls one.

## Components

- Consul (Service Registry)
- service.py (Service Instance)
- client.py (Client Service)

## Running the Project

1. Start Consul

consul agent -dev

2. Start service instances

python service.py 5001  
python service.py 5002

3. Run client

python client.py

The client will randomly call one of the service instances.