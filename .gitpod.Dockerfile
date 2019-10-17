FROM gitpod/workspace-full

USER root


# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
RUN apt-get update \
    && apt-get install -y castxml \
    && apt install -y freeglut3-dev \
    && apt install -y binutils-gold g++ cmakelibglew-dev g++ mesa-common-dev build-essential libglew1.5-dev libglm-dev
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
