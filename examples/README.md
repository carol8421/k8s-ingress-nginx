# Examples

## Prerequisites

* Multinode cluster running Kubernetes 1.2
* You've build and made available ndslabs/nginx-ingress-controller
* At least one node with label=ingresslb
* Wildcard CNAME entry \*.ndslabs.org pointing to the IP address of the loadbalancer
* demo namespace running the ELK stack
* terra namespace running Clowder stack

## Running the examples

1. Create the default-http-backend resource to handle 404 errors

```
kubectl create -f default-backend.yaml
```

1. Create the nginx ingress controller (load balancer)

```
kubectl create -f loadbalancer-rc.yaml
```

1. Create the ingress rules for the base ndslabs services

```
kubectl create -f default-ingress.yaml
```

1. Create the ingress rules for the demo and terra namespaces. You will need to modify these yaml files with the correct service names:

```
kubectl create -f demo-ingress.yaml
kubectl create -f terra-ingress.yaml
```

1. Open your browser to elk.demo.ndslabs.org and clowder.terra.ndslabs.org


##  TLS example

1. Crete a wildcard certificate for test.ndslabs.org

```
openssl genrsa 2048 > ndslabs.key
openssl req -new -x509 -nodes -sha1 -days 3650 -key ndslabs.key > ndslabs.cert
#[enter *.ndslabs.org for the Common Name]
openssl x509 -noout -fingerprint -text < ndslabs.cert > ndslabs.info
cat ndslabs.cert ndslabs.key > ndslabs.pem
chmod 400 ndslabs.key ndslabs.pem
```

1. Create a secret with SSL certificate and key
```
./gensecret.sh
kubectl create -f secret.yaml
```

1. Create ingress rules for demo project with TLS

```
kubectl create -f demo-ingress-tls.yaml
```
