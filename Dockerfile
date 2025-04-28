FROM registry.access.redhat.com/ubi9/python-311:latest

WORKDIR /mcp_server

# Install MCP CLI
RUN pip install mcp["cli"]

# Clone the ServiceNow MCP repository
RUN git clone https://github.com/michaelbuckner/servicenow-mcp.git /tmp/servicenow-mcp

# Install from the cloned repository
WORKDIR /tmp/servicenow-mcp
RUN pip install -e .

# Return to our working directory
WORKDIR /mcp_server

# Expose the port
EXPOSE 8000

# Use the recommended command with environment variables for credentials
# and explicitly use SSE transport for containerized environments
ENTRYPOINT ["python", "-m", "mcp_server_servicenow.cli", "--transport", "sse"]
