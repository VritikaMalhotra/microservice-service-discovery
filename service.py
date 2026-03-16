from flask import Flask
import consul
import socket
import sys

app = Flask(__name__)

# get port from command line
port = int(sys.argv[1])

# create consul connection
c = consul.Consul()

# create unique service id
service_id = socket.gethostname() + "-" + str(port)

# register service in consul
c.agent.service.register(
    name="my-service",
    service_id=service_id,
    address="localhost",
    port=port
)

@app.route("/")
def hello():
    return f"Hello from service running on port {port}"

app.run(port=port)