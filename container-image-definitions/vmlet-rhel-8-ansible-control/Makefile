CONTAINER_NAME=vmlet-rhel-8-ansible-control
RHEL_VERSION=8.3
SSH_PORT=2222
# REGISTRY=docker.io/tonykay
REGISTRY=quay.io/tonykay

# make list: list all options

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# EXTRA_ARGS='--squash' for example


help:
	echo "Best executed make help -s"
	echo
	echo "help:               Show this help, best executed make help -s"
	echo "build:              Do a docker based build"
	echo "                      make build EXTRA_ARGS='--squash'"
	echo "build-epel:         Do a docker based build using a Dockerfile with EPEL"
	echo "                      make build-epel EXTRA_ARGS='--squash'"
	echo "tag:                Tag the image"
	echo "scan:               Scan an image using synk"
	echo "push:               Push an image"
	echo "complete:           build scan tag push - Do a complete build to push workflow"
	echo "build2push:         same as 'complete'"
	echo "docker-login:       Login to registry via docker command"
	echo "podman-login:       Login to registry via podman command"
	echo "run:                Run image via docker with sensible defaults, alias for docker-run"
	echo "docker-run:         Run image via docker with sensible defaults"
	echo "podman-run:         Run image via podman with sensible defaults"
	echo "docker-attach:      Attach to *RUNNING* container via 'docker exec -it"
	echo "podman-attach:      Attach to *RUNNING* container via 'podman exec -it"
	echo "docker-run-shell:   Run image via docker with sensible defaults"
	echo "podman-run-shell:   Run image via podman with sensible defaults"

#docker-kill:


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

complete: build2push

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
	
docker-attach:
	docker exec -it ${CONTAINER_NAME} sudo su - devops

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

#complete: build scan tag push
#
#build:
#	DOCKER_BUILDKIT=1 \
#		docker build \
#		-f Dockerfile \
#		-t ${CONTAINER_NAME} \
#		--build-arg=RHEL_VERSION=${RHEL_VERSION} \
#		--squash .
#
#build-epel:
#	DOCKER_BUILDKIT=1 \
#		docker build \
#		-f Dockerfile-vmlet-rhel-8-epel \
#		-t ${CONTAINER_NAME}-epel \
#		--build-arg=RHEL_VERSION=${RHELVERSION} \
#		--squash .
#
#run:
#	docker run \
#		-d \
#		--privileged \
#		--name ${CONTAINER_NAME} \
#		--hostname ${CONTAINER_NAME} \
#		--rm \
#		-p ${SSH_PORT}:22 \
#		${CONTAINER_NAME} 
#
#run-shell:
#	docker run \
#		-it \
#		--rm \
#		--privileged \
#		--name ${CONTAINER_NAME} \
#		--hostname ${CONTAINER_NAME} \
#		${CONTAINER_NAME} 
