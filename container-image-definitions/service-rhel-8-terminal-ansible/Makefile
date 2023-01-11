IMAGE_NAME								= service-rhel-8-terminal-ansible
REGISTRY									= docker.io/tonykay
CONTAINER_RUNTIME				 	= docker

CONTAINER_HOSTNAME				= control
RHEL_VERSION							= 8.7
SSH_PORT									= 2223
TERMINAL_PORT						 = 8888
SHELL_COMMAND						 = sudo su - devops

# CONTAINER_NAME=service-rhel-8-terminal-ld-multi : ## Do a docker based build

build-multi : ## Do a docker based build
build-multi : ##		EXTRA_ARGS='--squash --no-cache' for example
	docker buildx build \
    --platform linux/arm64/v8,linux/amd64 \
    --tag $(REGISTRY)/$(IMAGE_NAME):$${VERSION:-latest} \
    --push \
    $(EXTRA_ARGS) .

build:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t ${CONTAINER_NAME} \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		${EXTRA_ARGS} .
#		--no-cache	

build-squash:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t ${CONTAINER_NAME} \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		--no-cache \
		--squash .

build-epel:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-epel \
		-t ${CONTAINER_NAME}-epel \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} .

build-epel-squash:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-epel \
		-t ${CONTAINER_NAME}-epel \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		--squash .

run:
	docker run \
		-d \
		--privileged \
		--name terminal \
		--hostname terminal \
		--rm \
		-p ${TERMINAL_PORT}:8080 \
		${CONTAINER_NAME} 

run-shell:
	docker run \
		-it \
		--rm \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} bash 


list:
	ls ${EXTRA}
