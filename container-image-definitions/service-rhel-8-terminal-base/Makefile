IMAGE_NAME=service-rhel-8-terminal-base
CONTAINER_NAME=terminal


RHEL_VERSION=8.3
TERMINAL_PORT=8080

# REGISTRY=docker.io/tonykay
REGISTRY=quay.io/tonykay

: ## TIP! make supports tab completion with *modern* shells e.g. zsh etc
: ##  

help: ## Show this help - technically unnecessary as `make` alone will do 
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Thanks to victoria.dev for the above syntax
# https://victoria.dev/blog/how-to-create-a-self-documenting-makefile/

build: ## Do a docker based build
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t ${CONTAINER_NAME} \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		${EXTRA_ARGS} .


build-epel: ## Do a docker based build using a Dockerfile with EPEL
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-vmlet-rhel-8-epel \
		-t ${CONTAINER_NAME}-epel \
		--build-arg=RHEL_VERSION=${RHELVERSION} \
		${EXTRA_ARGS} .


tag: ## Tag the image
	docker tag ${CONTAINER_NAME} ${REGISTRY}/${CONTAINER_NAME}:latest

push: ## Push the image to remote registry
	docker push ${REGISTRY}/${CONTAINER_NAME}:latest

scan: ## Scan an image using synk
	docker scan ${CONTAINER_NAME} \

complete: build scan tag push ## build -> scan -> tag -> push - Do a complete build to push workflow

docker-login: ## Login to registry via docker command
	docker login ${REGISTRY}

podman-login: Login to registry via podman command 
	podman login ${REGISTRY}

docker-run: ## Run image via docker with sensible defaults
	docker run \
		-d \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		--rm \
		-p ${SSH_PORT}:22 \
		${CONTAINER_NAME} 

podman-run: ## Run image via podman with sensible defaults
	podman run \
		-d \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		--rm \
		-p ${SSH_PORT}:22 \
		${REGISTRY}/${CONTAINER_NAME}:latest

docker-run-shell: ## Run image via docker with sensible defaults
	docker run \
		-it \
		--rm \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} sudo su - devops

podman-run-shell: ## Run image via podman with sensible defaults
	docker run \
		-it \
		--rm \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} sudo su - devops

docker-attach: ## Attach to a container via docker with the devops user shell
	docker exec -it ${CONTAINER_NAME} sudo su - devops

podman-attach: ## Attach to a container via podman with the devops user shell
	docker exec -it ${CONTAINER_NAME} sudo su - devops

