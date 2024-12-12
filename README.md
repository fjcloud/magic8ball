# Magic8ball

## Build / Deploy on OpenShift

```shell
oc new-project magic8ball
oc new-app https://github.com/fjcloud/magic8ball.git --strategy docker
```
