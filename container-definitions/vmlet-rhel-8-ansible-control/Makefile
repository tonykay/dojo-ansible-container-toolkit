RHEL_VERSION=8.3
SSH_PORT=2222
CONTAINER_NAME=vmlet-rhel-8-ansible-control

build:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t ${CONTAINER_NAME} \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		--squash .

build-epel:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-vmlet-rhel-8-epel \
		-t ${CONTAINER_NAME}-epel \
		--build-arg=RHEL_VERSION=${RHELVERSION} \
		--squash .

run:
	docker run \
		-d \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		--rm \
		-p ${SSH_PORT}:22 \
		${CONTAINER_NAME} 

run-shell:
	docker run \
		-it \
		--rm \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} 
