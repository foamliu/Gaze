from kubernetes import client, config
from settings import CURRENT_FOLDER

config.load_kube_config(config_file=CURRENT_FOLDER + "/config")

v1=client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))