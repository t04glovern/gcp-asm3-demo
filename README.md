# Animal Shelter Manager (GCP Demo)

Going through the steps required to migrate and host Animal Shelter Manager (ASM3) on Google Cloud.

## Setup

Pull down project submodules

```bash
git clone https://github.com/t04glovern/gcp-asm3-demo.git
cd gcp-asm3-demo
git submodule update --init --recursive
```

## Instructions

- [01 - GCP Setup](instructions/01-gcp-setup.md)
- [02 - GCP Kubernetes Setup](instructions/02-gcp-kubernetes-setup.md)
- [03 - Build ASM3 Docker](instructions/03-asm3-docker.md)
- [04 - GCR Setup](instructions/04-gcr-setup.md)
- [05 - Pod Deployment](instructions/05-pod-deploy.md)
- [06 - Helm Setup [TODO]](instructions/06-helm-setup.md)

## Attribution

- [Google Cloud SDK Setup](https://cloud.google.com/sdk/install)
- [mkjelland/spring-boot-postgres-on-k8s-sample](https://github.com/mkjelland/spring-boot-postgres-on-k8s-sample)