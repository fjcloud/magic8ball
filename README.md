# Magic8ball

## Build / Deploy on OpenShift

```shell
oc new-project magic8ball
oc new-app https://github.com/fjcloud/magic8ball.git --strategy docker
oc create route edge --service=magic8ball
```

## Use the hardened Python image

```shell
oc patch bc/magic8ball --type=merge -p '{"spec":{"strategy":{"dockerStrategy":{"from":{"kind":"DockerImage","name":"registry.access.redhat.com/hi/python:3.14"}}}}}'
oc start-build magic8ball
```
