RHEL_VERSION=8.3
TERMINAL_PORT=8080
CONTAINER_NAME=service-rhel-8-terminal-ansible

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
