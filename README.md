## Python API Template

This repo is a template for a python api with Flask


### Configure & Install

Configure `config.yml` 

**Optional** To generate only the configuration files

```bash
make config
```

To run container on port 5005

```bash
make build
```

To run the container with traefik proxy and letsencrypt

```bash
make traefik
```

**Note:** If you are running this locally you won't be able to get a cert from letsencrypt
You should then build for local

```bash
make local
```

If you want to stop all containers

```bash
make stop
```

If you want to remove all generated config files
```bash
make clean
```


### Issues

If you have any questions or issues please open an issue on this repo
