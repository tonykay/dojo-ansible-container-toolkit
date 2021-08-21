ARG ARCH=

FROM ${ARCH}alpine

ARG REPO_ARCH=
ENV REPO_ARCH=$REPO_ARCH 
#FROM ${ARCH}debian:buster-slim

COPY hello.txt /hello.txt
RUN echo ${REPO_ARCH}-hello >> /hello.txt
RUN echo ${ARCH}-hello >> /hello.txt

CMD ["echo"]
