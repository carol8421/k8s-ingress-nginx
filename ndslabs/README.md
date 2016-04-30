# NDSLabs NGINX Ingress Controller - Prototype

## Setup and Deploy
* Allocate one kubernetes node with private and public addresses
* label the node as the ingress node:  
```
kubectl label nodes <private-address> ndslabs-role=ingresslb
```
* deploy the controller:  
```
kubectl create -f ndslabs-ingress.yml
```

## Tests 
* Deploy nginx-hello's for 2 copies of 2 services - coffee and tea:  
* kubectcl create -f tests/services/tea.yml && kubectcl create -f tests/services/coffee.yml

## Host/Path routing - without DNS
* Deploy the ingress mappings for beverages.ndslabs.org/{coffee,tea}:  
* Curl with DNS resolution imitation: 
```
kubectl create -f tests/beverages.yml
curl --resolve beverages.nds.org:80:<public-ip> http://beverages.ndslabs.org/tea
curl --resolve beverages.nds.org:80:<public-ip> http://beverages.ndslabs.org/coffee
```
* Tear down the beverage mappings
```
kubectl delete ingress beverages
```

## Host/Path routing - with DNS records
*  Same as without DNS, but create NDS records to point to the public IP, and use
the DNS names instead of beverages.nds.org - example is foo.ndslabs.org
* Copy and edit beverages.yml - replace beverages.nds.org with your DNS name
* Curl directly: 
```
kubectl create -f tests/mybeverages.yml
curl http://<my-dns>/tea
curl http://beverages.ndslabs.org/coffee
```

## TLS self-signed, no DNS
* Make a self signed cert:
```
python makesecret.py beverage-secret
```
* Deploy the Ingress with TLS
```
* kubectl create -f beverage-secret.yml
```
* Curl: ignore self-signed: 
```
curl --resolve beverages.nds.org:80:<public-ip> http://beverages.ndslabs.org/tea --insecure
curl --resolve beverages.nds.org:80:<public-ip> http://beverages.ndslabs.org/coffee --insecure
```
* Tear down the beverage mappings
```
kubectl delete ingress beverages
```

## TLS with DNS
* Obtain TLS certs for your DNS name, copy and edit the key and crt in beverage-secrets.yml
* Deploy the  TLS secret
```
* kubectl create -f beverage-secret.yml
```
* Curl: 
```
kubectl create -f tests/beverages.yml
curl --resolve beverages.nds.org:80:<public-ip> http://beverages.ndslabs.org/tea
curl --resolve beverages.nds.org:80:<public-ip> http://beverages.ndslabs.org/coffee
```
* Tear down the beverage mappings
```
kubectl delete ingress beverages
```
