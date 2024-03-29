# GCP Kubernetes Setup

## Create Cluster

We'll start by firing up a new GKE cluster

```bash
# https://cloud.google.com/sdk/gcloud/reference/container/clusters/create
# `gcloud container get-server-config` to get a machine type list
gcloud container clusters create devopstar-gke-clst-1 \
    --num-nodes 2 \
    --cluster-version 1.12.6-gke.7 \
    --machine-type g1-small \
    --region australia-southeast1
```

## Connect to Existing

You can grab the connection command from the [GKE console](https://console.cloud.google.com/kubernetes/list) but it should look like something similar to below (replace the project name obviously).

```bash
gcloud container clusters get-credentials devopstar-gke-clst-1 \
    --region australia-southeast1 \
    --project arctic-bee-236107
```

## Get Info

### Cluster Info

```bash
$ kubectl cluster-info
# Kubernetes master is running at https://XXX.XXX.XXX.XXX
# GLBCDefaultBackend is running at https://XXX.XXX.XXX.XXX/api/v1/namespaces/kube-system/services/default-http-backend:http/proxy
# Heapster is running at https://XXX.XXX.XXX.XXX/api/v1/namespaces/kube-system/services/heapster/proxy
# KubeDNS is running at https://XXX.XXX.XXX.XXX/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
# Metrics-server is running at https://XXX.XXX.XXX.XXX/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy
```

### Get Nodes

```bash
$ kubectl get nodes
# NAME                                                  STATUS   ROLES    AGE   VERSION
# gke-devopstar-gke-clst-1-default-pool-2e1439f4-hr9s   Ready    <none>   58s   v1.12.6-gke.7
# gke-devopstar-gke-clst-1-default-pool-2e1439f4-pnqj   Ready    <none>   1m    v1.12.6-gke.7
# gke-devopstar-gke-clst-1-default-pool-5a44aa0a-cdml   Ready    <none>   56s   v1.12.6-gke.7
# gke-devopstar-gke-clst-1-default-pool-5a44aa0a-lcb8   Ready    <none>   53s   v1.12.6-gke.7
# gke-devopstar-gke-clst-1-default-pool-5b4726d0-ndwj   Ready    <none>   1m    v1.12.6-gke.7
# gke-devopstar-gke-clst-1-default-pool-5b4726d0-nw85   Ready    <none>   1m    v1.12.6-gke.7
```

### Kubctl Config

You can view the kubctl configuration being used by running

```bash
$ kubectl config view
# apiVersion: v1
# clusters:
# - cluster:
#     certificate-authority-data: DATA+OMITTED
#     server: https://XXX.XXX.XXX.XXX
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
