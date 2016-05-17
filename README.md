# NGINX Ingress Controller for NDSLabs

This is an implementation of an [Ingress Controller](https://github.com/kubernetes/contrib/tree/master/ingress/controllers) for use with the [NDS Labs](https://github.com/nds-org/ndslabs) services.  It is an adaptation of the [Kubernetes NGINX Ingress Controller](https://github.com/kubernetes/contrib/tree/master/ingress/)

## Overview
This NGINX ingress controller serves as a load-balancer for services deployed using NDS Labs. Since it is a DNS name-based solution, it requires an existing DNS entry for the cluster (e.g., cluster.ndslabs.org).

This service consists of the following:
* Load balancer: NGINX ingress controller (docker image)
* Ingress rules: Kubernetes Ingress resource defining service mappings for a namespace/project
* TLS/Secrets: Either a wildcard certificate or per-service certificates stored as Kubernetes secrets

## Building the controller image

To build the Docker image for the ingress controller:
```
cd controllers/nginx
make controller
make push
```

## Creating the load balancer and ingress rules

See the [examples](examples/README.md) for instructions on deploying the NGINX load balancer and associated Ingress rules for NDS Labs
