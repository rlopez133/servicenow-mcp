# ServiceNow MCP for OpenShift

This repository contains the files needed to run the ServiceNow MCP server in OpenShift.

## File

**Dockerfile** - Container definition for OpenShift to build the ServiceNow MCP server

## Deployment

Simply use OpenShift's build capabilities to build and deploy:

```bash

# Create a new project
oc new-project snow-mcp

# Create a new build using this repository
oc new-build --strategy=docker --name=servicenow-mcp https://github.com/rlopez133/servicenow-mcp.git

# Start the build process
oc start-build servicenow-mcp --follow

# Create secret with ServiceNow credentials
oc create secret generic servicenow-credentials \
  --from-literal=SERVICENOW_INSTANCE_URL=https://your-instance.service-now.com/ \
  --from-literal=SERVICENOW_USERNAME=your-username \
  --from-literal=SERVICENOW_PASSWORD=your-password

# Create the app from the build
oc new-app servicenow-mcp

# Link secret to deployment
oc set env deployment/servicenow-mcp --from=secret/servicenow-credentials

# Expose the service
oc expose service/servicenow-mcp --port=8000
```

OpenShift will build the container from the Containerfile and deploy it.
