FROM jenkins/jenkins:lts

USER root

# Cài đặt git, docker và docker-compose
RUN apt-get update && \
    apt-get install -y git docker.io docker-compose && \
    usermod -aG docker jenkins

USER jenkins

