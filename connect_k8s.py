from kubernetes import client, config
from settings import CURRENT_FOLDER

config.load_kube_config(config_file=CURRENT_FOLDER + "/config")
v1 = client.CoreV1Api()
extensions_v1beta1 = client.ExtensionsV1beta1Api()

def list_all_pods():
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def create_deployment_object(package_name):
    # Configureate Pod template container
    container = client.V1Container(
        name=package_name,
        image="gazetest/" + package_name,
        ports=[client.V1ContainerPort(container_port=80)])

    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": package_name + "-pod"}),
        spec=client.V1PodSpec(containers=[container]))

    # Create the specification of deployment
    spec = client.ExtensionsV1beta1DeploymentSpec(
        replicas=1,
        template=template)

    # Instantiate the deployment object
    deployment = client.ExtensionsV1beta1Deployment(
        api_version="extensions/v1beta1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=package_name + "-deploy"),
        spec=spec)

    return deployment


def create_deployment(deployment):
    # Create deployement
    api_response = extensions_v1beta1.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))
