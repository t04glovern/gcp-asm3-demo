# Pod Deployment

## Deploy Postgres

```bash
kubectl apply -f ./specs/postgres.yml
```

## Deploy ASM3

```bash
kubectl apply -f ./specs/asm3.yml
```

Then, once the load balancer has come up, run the following to retrieve the public IP

```bash
kubectl get svc asm3-lb -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
```

Then update the `specs/asm3.yml` ConfigMap file on line 11 and 15 to use the IP instead of `localhost`

```bash
...

# The base URL to the ASM installation as seen by the client (should not end with /)
base_url = http://<loadBalancer_ip>

# The URL to asm's service endpoint to be shown in online forms screen
# (typically base_url + /service)
service_url = http://<loadBalancer_ip>/service

...
```

This complexity is due to the way the application was written (needing the clients address for access is not typical of software usually).

## Cleanup

```bash
kubectl delete -f ./specs/asm3.yml
kubectl delete -f ./specs/postgres.yml
```