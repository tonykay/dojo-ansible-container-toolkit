RHEL_VERSION=8.3
TERMINAL_PORT=8080
IMAGE_NAME=service-rhel-8-terminal-base
CONTAINER_NAME=terminal

build:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t ${IMAGE_NAME} \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		${EXTRA_ARGS} .

build-epel:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-epel \
		-t ${IMAGE_NAME}-epel \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		--no-cache \
		${EXTRA_ARGS} .
# 		--squash .

run:
	docker run \
		-d \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		--rm \
		-p ${TERMINAL_PORT}:8080 \
		${IMAGE_NAME} \

		# --privileged \

shell:
	docker exec -it \
	${CONTAINER_NAME} bash
	
run-shell:
	docker run \
		-it \
		--rm \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} bash 
