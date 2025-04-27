# ServiceNow MCP for OpenShift

This repository contains the files needed to run the ServiceNow MCP server in OpenShift.

## Files

1. **Containerfile** - Container definition for OpenShift to build the ServiceNow MCP server
2. **start.py** - Script to initialize and run the MCP server with SSE transport

## Deployment

Simply use OpenShift's build capabilities to build and deploy these files:

```bash
# Create a new build using this repository
oc new-build --strategy=docker --name=servicenow-mcp https://github.com/rlopez133/servicenow-mcp-openshift.git

# Create the app from the build
oc new-app servicenow-mcp

# Create secret for ServiceNow credentials
oc create secret generic servicenow-credentials \
  --from-literal=SERVICENOW_INSTANCE_URL=https://your-instance.service-now.com/ \
  --from-literal=SERVICENOW_USERNAME=your-username \
  --from-literal=SERVICENOW_PASSWORD=your-password

# Link secret to deployment
oc set env deployment/servicenow-mcp --from=secret/servicenow-credentials

# Expose the service
oc expose service/servicenow-mcp --port=8001
```

OpenShift will build the container from the Containerfile and deploy it.
