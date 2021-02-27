FROM gitpod/workspace-full:latest

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py \
    && python3 get-poetry.py --yes
