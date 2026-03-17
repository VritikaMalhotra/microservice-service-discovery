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

## Optional: Service Mesh Discovery

In larger distributed systems, service discovery can also be implemented using a service mesh such as Istio or Linkerd. 
In a service mesh architecture, each service runs alongside a sidecar proxy. 

Instead of the client directly handling service discovery and routing, communication flows as:

App → Sidecar Proxy → Service Mesh → Sidecar Proxy → App

The sidecar proxies handle:

- Traffic routing (load balancing, version routing)
- Observability (metrics, logging, tracing)
- Security (mTLS encryption between services)

This approach removes networking logic from application code and provides better control, monitoring, and security in large-scale microservice environments.