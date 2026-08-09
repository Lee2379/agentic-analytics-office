#!/usr/bin/env bash
set -euo pipefail

container="${HERMES_CONTAINER:-hermes-docker}"
profiles=(ada ethan mia noah oliver sam sophie)

printf '%s\n' '=== COLLECTION POLICY ==='
printf '%s\n' 'Read credential values: no'
printf '%s\n' 'Read private prompts or sessions: no'
printf '%s\n' 'Modify runtime: no'

printf '\n%s\n' '=== RUNTIME VERSION ==='
docker exec --user hermes "$container" hermes --version

printf '\n%s\n' '=== EVIDENCE IDENTITY ==='
docker exec --user hermes "$container" id

printf '\n%s\n' '=== CONTAINER CONTROLS ==='
docker inspect "$container" --format 'Image={{.Config.Image}}
Status={{.State.Status}}
RestartPolicy={{.HostConfig.RestartPolicy.Name}}
MemoryBytes={{.HostConfig.Memory}}
NanoCPUs={{.HostConfig.NanoCpus}}
PublishedPorts={{json .NetworkSettings.Ports}}'

mount_destinations="$(docker inspect "$container" --format '{{range .Mounts}}{{.Destination}} {{end}}')"
printf 'MountDestinations=%s\n' "$mount_destinations"
if [[ " $mount_destinations " == *" /var/run/docker.sock "* ]]; then
  printf '%s\n' 'DockerSocketMounted=yes'
else
  printf '%s\n' 'DockerSocketMounted=no'
fi

printf '\n%s\n' '=== PROFILE SUMMARIES ==='
for profile in "${profiles[@]}"; do
  docker exec --user hermes "$container" hermes profile show "$profile"
done

printf '\n%s\n' '=== COLLECTOR GUARANTEES ==='
printf '%s\n' 'Credential values read: no'
printf '%s\n' 'Private messages read: no'
printf '%s\n' 'System modifications performed: no'
