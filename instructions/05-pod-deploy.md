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

This complexity is due to the way the application was written (needing the clients address for access is not typical of software usually). Run the apply command again.

```bash
kubectl apply -f ./specs/postgres.yml
```

Now we need to force restart the pod, and since the pod is part of a ReplicaSet we can just delete the existing on and a new one will be created in its place.

```bash
$ kubectl get pods
# NAME                        READY   STATUS    RESTARTS   AGE
# asm3-66c67fbf77-qxlp4       1/1     Running   0          4m42s
# postgres-78ffddbdc5-xjggf   1/1     Running   0          5m3s
```

Use the pods name in the following command to delete it

```bash
$ kubectl delete pod asm3-66c67fbf77-qxlp4
# pod "asm3-66c67fbf77-qxlp4" deleted
```

## Cleanup

```bash
# Delete deployments
kubectl delete -f ./specs/asm3.yml
kubectl delete -f ./specs/postgres.yml

# Delete cluster
gcloud container clusters delete devopstar-gke-clst-1 \
    --region australia-southeast1 \
    --project arctic-bee-236107
```

Optionally delete the GCR image

```bash
# Syntax
gcloud container images delete [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[TAG] --force-delete-tags

# Example
gcloud container images delete asia.gcr.io/arctic-bee-236107/asm3:latest --force-delete-tags
```