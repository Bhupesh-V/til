<!-- omit from toc -->
# How to run a Local Nomad Cluster

- [Pre-requisties](#pre-requisties)
- [Start Nomad Agent](#start-nomad-agent)
  - [Check Nomad Agent Status](#check-nomad-agent-status)
- [Start Consul Agent](#start-consul-agent)
- [Submit a Job](#submit-a-job)
- [Common Issues](#common-issues)
  - [Nomad doesn’t reference local docker image](#nomad-doesnt-reference-local-docker-image)
  - [`port_map' cannot map group network ports, use 'ports' instead`](#port_map-cannot-map-group-network-ports-use-ports-instead)
  - [`Constraint ${attr.consul.version} semver >= 1.8.0 filtered 1 node`](#constraint-attrconsulversion-semver--180-filtered-1-node)
  - [Nomad can’t connect to docker daemon - docker driver missing from nomad agent stats (MacOS)](#nomad-cant-connect-to-docker-daemon---docker-driver-missing-from-nomad-agent-stats-macos)
  - [API Error - (500) Permission Denied `mkdir /host_mnt/private/tmp/ permission denied nomad` (MacOS)](#api-error---500-permission-denied-mkdir-host_mntprivatetmp-permission-denied-nomad-macos)
- [Tips](#tips)


## Pre-requisties

1. Start Docker Daemon if not already running.
2. Check if you have the following commands accessible.
   1. Nomad (`nomad --version`)
   2. Consul (`consul --version`)

## Start Nomad Agent

```
sudo nomad agent -dev \
  -bind 0.0.0.0 \
  -network-interface='{{ GetDefaultInterfaces | attr "name" }}'
```

### Check Nomad Agent Status

In a separate terminal, check agenet status

```
export NOMAD_ADDR=http://localhost:4646

nomad node status
```

or verbose version with detailed breakdown

```
nomad node status -self -verbose
```

Check Web UI for more info: [http://localhost:4646/ui](http://localhost:4646/ui)

## Start Consul Agent

In a separate terminal, start consul.

```
consul agent -dev
```

## Submit a Job

```
nomad job run -address=http://localhost:4646 deploy.nomad
```

## Common Issues

### Nomad doesn’t reference local docker image

1. The tag for the image should be local. 
2. Ref: How can I make a nomad job use a local docker image?

### `port_map' cannot map group network ports, use 'ports' instead`

Use the new ports approach like this

```hcl
group "app" {
  network {
    port "http" { 
      to = 8080
    }
  }

  task "example" {
    driver = "docker"

    config {
      ports = ["http"]
    }
  }
}
```

### `Constraint ${attr.consul.version} semver >= 1.8.0 filtered 1 node`

1. Make sure the consul agent is running. Start it by consul agent -dev. 
2. Follow these steps in case of above issue
   1. `consul agent -dev -bind 0.0.0.0 -log-level INFO`
   2. `sudo nomad agent -dev -bind 0.0.0.0 -log-level INFO`
   3. `nomad job run example.nomad`
3. Ref: https://github.com/hashicorp/waypoint/issues/3376 

### Nomad can’t connect to docker daemon - docker driver missing from nomad agent stats (MacOS)

1. Enable default docker socket
2. Ref: https://stackoverflow.com/a/76219883 
   1. Make sure the following command runs successfully. If not disable the socket access on Docker Dashboard & re-nable it again (forces socket file creation)
   ```
   ls /var/run/docker.sock
   ```

### API Error - (500) Permission Denied `mkdir /host_mnt/private/tmp/ permission denied nomad` (MacOS)

1. Change virtualization framework from VirtioFS to gRPC Fuse in Docker Desktop
2. Ref: https://stackoverflow.com/a/78276263 

## Tips

1. When accessing processes on host computer, use `host.docker.internal`



