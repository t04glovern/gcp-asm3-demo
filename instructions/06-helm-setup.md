# Helm Setup

## Install Helm

For Linux you can follow the instructions below. For other OS's use the instructions at [https://helm.sh/docs/using_helm/#installing-helm](https://helm.sh/docs/using_helm/#installing-helm)

```bash
# Latest version from: https://github.com/helm/helm/releases
wget https://storage.googleapis.com/kubernetes-helm/helm-v2.13.1-linux-amd64.tar.gz
tar -zxvf helm-v2.13.1-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm
rm -r linux-amd64 && rm helm-v2.13.1-linux-amd64.tar.gz
```