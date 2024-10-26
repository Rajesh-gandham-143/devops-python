import docker

client=docker.from_env()

def count_containers():
    containers=client.containers.list()
    print("running containers")
    for i,container in enumerate(containers):
        print(f"{i}: {container.name} (ID: {container.short_id})")
        return containers
    
count_containers()