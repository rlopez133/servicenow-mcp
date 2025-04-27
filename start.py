#!/usr/bin/env python
"""
Start script for ServiceNow MCP in containers
"""
import os
import sys
from mcp_server_servicenow.server import ServiceNowMCP, create_basic_auth, create_token_auth, create_oauth_auth

# Get connection details from environment variables
instance_url = os.environ.get("SERVICENOW_INSTANCE_URL")
username = os.environ.get("SERVICENOW_USERNAME")
password = os.environ.get("SERVICENOW_PASSWORD")
token = os.environ.get("SERVICENOW_TOKEN")
client_id = os.environ.get("SERVICENOW_CLIENT_ID")
client_secret = os.environ.get("SERVICENOW_CLIENT_SECRET")

# Check for required URL
if not instance_url:
    print("Error: SERVICENOW_INSTANCE_URL environment variable is required", file=sys.stderr)
    sys.exit(1)

# Set up authentication based on available credentials
auth = None
if token:
    auth = create_token_auth(token)
elif client_id and client_secret and username and password:
    auth = create_oauth_auth(client_id, client_secret, username, password, instance_url)
elif username and password:
    auth = create_basic_auth(username, password)
else:
    print("Error: Authentication credentials required", file=sys.stderr)
    print("Set either SERVICENOW_USERNAME and SERVICENOW_PASSWORD, or SERVICENOW_TOKEN", file=sys.stderr)
    sys.exit(1)

# Create and run the server with SSE transport
server = ServiceNowMCP(instance_url=instance_url, auth=auth)
server.run(transport="sse")
