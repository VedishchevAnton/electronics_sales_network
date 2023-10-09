FROM ubuntu:latest
LABEL authors="Vedis"

ENTRYPOINT ["top", "-b"]