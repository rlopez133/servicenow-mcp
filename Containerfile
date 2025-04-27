FROM registry.access.redhat.com/ubi9/python-311:latest

WORKDIR /mcp_server

COPY start.py /mcp_server/

EXPOSE 8001

RUN pip install mcp["cli"]
RUN pip install mcp-server-servicenow

ENTRYPOINT ["python", "start.py"]
