# ASM3 Docker Container

I helped by building a Docker pipeline for Animal Shelter Manager that's been merged into master branch at [https://github.com/bobintetley/asm3](https://github.com/bobintetley/asm3)

For this repo we've included it as a submodule in `asm3`

## Overview

Local testing / development environment for ASM3 can be achieved with Docker. This stack creates two containers:

- **postgres**: Simple postgres database
  - user: asm3
  - pass: asm3
  - db: asm
- **asm3**: ASM3 application running in container. Configurations defined in [lib/asm3.conf.local](../lib/asm3.conf.local)

## Get Started

### Containers Up

```bash
docker-compose up -d
```

Open [http://localhost:5000](http://localhost:5000) to view the running application

**NOTE:** *There is a rare issue with running it from localhost where existing cookies break the application. To fix simply remove any local cookies*

### Containers Down

```bash
docker-compose down -v
```

## Non-compose build

If you need to build without docker-compose, simply run the following

```bash
docker build -t asm3 ./asm3
```
