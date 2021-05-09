CONTAINER_NAME=vmlet-rhel-8-base

RHEL_VERSION=8.3
SSH_PORT=2222
# REGISTRY=docker.io/tonykay
REGISTRY=quay.io/tonykay

# make list: list all options

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# EXTRA_ARGS='--squash' for example

build:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile \
		-t ${CONTAINER_NAME} \
		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
		${EXTRA_ARGS} .

build-epel:
	DOCKER_BUILDKIT=1 \
		docker build \
		-f Dockerfile-vmlet-rhel-8-epel \
		-t ${CONTAINER_NAME}-epel \
		--build-arg=RHEL_VERSION=${RHELVERSION} \
		${EXTRA_ARGS} .

tag:
	docker tag ${CONTAINER_NAME} ${REGISTRY}/${CONTAINER_NAME}:latest

push:
	docker push ${REGISTRY}/${CONTAINER_NAME}:latest

scan:
	docker scan ${CONTAINER_NAME} \

build2push: build scan tag push

docker-login:
	docker login ${REGISTRY}

podman-login:
	podman login ${REGISTRY}

run: docker-run

docker-run:
	docker run \
		-d \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		--rm \
		-p ${SSH_PORT}:22 \
		${CONTAINER_NAME} 

podman-run:
	podman run \
		-d \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		--rm \
		-p ${SSH_PORT}:22 \
		${REGISTRY}/${CONTAINER_NAME}:latest

docker-run-shell:
	docker run \
		-it \
		--rm \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} sudo su - devops

podman-run-shell:
	docker run \
		-it \
		--rm \
		--privileged \
		--name ${CONTAINER_NAME} \
		--hostname ${CONTAINER_NAME} \
		${CONTAINER_NAME} sudo su - devops

docker-kill:
	docker kill ${CONTAINER_NAME}
