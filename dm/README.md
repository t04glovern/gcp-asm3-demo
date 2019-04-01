# Deployment

## Kubeternetes Cluster

```bash
gcloud deployment-manager deployments create asm3 \
    --template gke-cluster.py \
    --properties zone:australia-southeast1-a
```

## Kubernetes Deployment

```bash
gcloud deployment-manager deployments create postgres-deployment \
    --template postgres-deployment.py \
    --properties clusterType:asm3-gke-cluster-py-type,image:postgres,port:5432
```