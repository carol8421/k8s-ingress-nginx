# NGINX Ingress Controller for NDSLabs

Implementation of [Ingress Controller](https://github.com/kubernetes/contrib/tree/master/ingress/controllers)
for [NGINX](http://nginx.org/) based on the [Kubernetes NGINX Ingress Controller](https://github.com/kubernetes/contrib/tree/master/ingress/)

## Building

```
cd controllers/nginx
make controller
make push
```

## Examples
See examples/README.md for instructions on deploying the NGINX load balancer and associated Ingress rules for NDS Labs
