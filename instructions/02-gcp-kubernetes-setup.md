# GCP Kubernetes Setup

We'll start by firing up a new GKE cluster

```bash
# https://cloud.google.com/sdk/gcloud/reference/container/clusters/create
gcloud container clusters create devopstar-gke-clst-1 \
    --num-nodes 2 \
    --machine-type f1-micro \
    --region australia-southeast1
```

## Get Info

### Cluster Info

```bash
$ kubectl cluster-info
# Kubernetes master is running at https://35.201.7.71
# GLBCDefaultBackend is running at https://35.201.7.71/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy
# Heapster is running at https://35.201.7.71/api/v1/namespaces/kube-system/services/heapster/proxy
# KubeDNS is running at https://35.201.7.71/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
# Metrics-server is running at https://35.201.7.71/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy
```

### Get Nodes

```bash
$ kubectl get nodes
# NAME                                                  STATUS   ROLES    AGE   VERSION
# gke-devopstar-gke-clst-1-default-pool-2e1439f4-hr9s   Ready    <none>   58s   v1.11.7-gke.12
# gke-devopstar-gke-clst-1-default-pool-2e1439f4-pnqj   Ready    <none>   1m    v1.11.7-gke.12
# gke-devopstar-gke-clst-1-default-pool-5a44aa0a-cdml   Ready    <none>   56s   v1.11.7-gke.12
# gke-devopstar-gke-clst-1-default-pool-5a44aa0a-lcb8   Ready    <none>   53s   v1.11.7-gke.12
# gke-devopstar-gke-clst-1-default-pool-5b4726d0-ndwj   Ready    <none>   1m    v1.11.7-gke.12
# gke-devopstar-gke-clst-1-default-pool-5b4726d0-nw85   Ready    <none>   1m    v1.11.7-gke.12
```

### Kubctl Config

You can view the kubctl configuration being used by running

```bash
$ kubectl config view
# apiVersion: v1
# clusters:
# - cluster:
#     certificate-authority-data: DATA+OMITTED
#     server: https://35.201.7.71
#   name: gke_arctic-bee-236107_australia-southeast1_devopstar-gke-clst-1
# contexts:
# - context:
#     cluster: gke_arctic-bee-236107_australia-southeast1_devopstar-gke-clst-1
#     user: gke_arctic-bee-236107_australia-southeast1_devopstar-gke-clst-1
#   name: gke_arctic-bee-236107_australia-southeast1_devopstar-gke-clst-1
# current-context: gke_arctic-bee-236107_australia-southeast1_devopstar-gke-clst-1
# kind: Config
# preferences: {}
# users:
# - name: gke_arctic-bee-236107_australia-southeast1_devopstar-gke-clst-1
#   user:
#     auth-provider:
#       config:
#         access-token: XXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#         cmd-args: config config-helper --format=json
#         cmd-path: /usr/lib/google-cloud-sdk/bin/gcloud
#         expiry: "2019-03-30T09:05:45Z"
#         expiry-key: '{.credential.token_expiry}'
#         token-key: '{.credential.access_token}'
#       name: gcp
```