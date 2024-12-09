# Magic8ball

## Deploy / Build on OpenShift

```shell
oc new-project magic8ball
oc new-app https://github.com/fjcloud/magic8bal --strategy dockerfile
```
