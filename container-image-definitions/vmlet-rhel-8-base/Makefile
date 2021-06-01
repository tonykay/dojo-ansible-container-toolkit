IMAGE_NAME=vmlet-rhel-8-base

REGISTRY 							= quay.io/tonykay
CONTAINER_RUNTIME 		= docker

CONTAINER_HOSTNAME 		= base
RHEL_VERSION 					= 8.4
SSH_PORT 							= 2222
SHELL_COMMAND 				= sudo su - devops

# Used instead of docker run.... bash 

: ## TIP! make supports tab completion with *modern* shells e.g. zsh etc
: ##  

help: ## Show this help - technically unnecessary as `make` alone will do 
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Thanks to victoria.dev for the above syntax
# https://victoria.dev/blog/how-to-create-a-self-documenting-makefile/

build : ## Do a docker based build
build : ##    EXTRA_ARGS='--squash --no-cache' for example
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t $(IMAGE_NAME) \
		--build-arg=RHEL_VERSION=$(RHEL_VERSION) \
		$(EXTRA_ARGS) .

build-epel : ## Do a docker based build using a Dockerfile with EPEL
build-epel : ##    EXTRA_ARGS='--squash' for example
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-vmlet-rhel-8-epel \
		-t $(IMAGE_NAME)-epel \
		--build-arg=RHEL_VERSION=$(RHEL_VERSION) \
		$(EXTRA_ARGS) .

tag : ## Tag the image
	docker tag $(IMAGE_NAME) $(REGISTRY)/$(IMAGE_NAME):latest

push : ## Push the image to remote registry
	docker push $(REGISTRY)/$(IMAGE_NAME):latest

scan : ## Scan an image using synk
	docker scan $(IMAGE_NAME) \

complete: build scan tag push ## build -> scan -> tag -> push - Do a complete build to push workflow

docker-login : ## Login to registry via docker command
	docker login $(REGISTRY)

podman-login: Login to registry via podman command 
	podman login $(REGISTRY)

docker-run : ## Run image via docker with sensible defaults
	$(CONTAINER_RUNTIME) run \
		-d \
		--privileged \
		--name $(CONTAINER_HOSTNAME) \
		--hostname $(CONTAINER_HOSTNAME) \
		--rm \
		-p $(SSH_PORT):22 \
		$(REGISTRY)/$(IMAGE_NAME) 

podman-run : ## Run image via podman with sensible defaults
podman-run : CONTAINER_RUNTIME = podman
podman-run : docker-run

docker-run-shell : ## Run image via docker with shell default in SHELL_COMMAND
	$(CONTAINER_RUNTIME) run \
		-it \
		--rm \
		--privileged \
		--name $(CONTAINER_HOSTNAME) \
		--hostname $(CONTAINER_HOSTNAME) \
		$(REGISTRY)/$(IMAGE_NAME) $(SHELL_COMMAND)

podman-run-shell : ## Run image via podman with shell default in SHELL_COMMAND
podman-run-shell : CONTAINER_RUNTIME = podman 
podman-run-shell : docker-run-shell

docker-attach : ## Attach to a container via docker with the devops user shell
	$(CONTAINER_RUNTIME) exec -it $(CONTAINER_HOSTNAME) $(SHELL_COMMAND)

podman-attach : ## Attach to a container via podman with the devops user shell
podman-attach : CONTAINER_RUNTIME = podman 
podman-attach : docker-attach
