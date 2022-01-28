FROM ubuntu:latest as builder

RUN apt-get update && apt-get install -y wget default-jdk-headless

ENV HADOOP_VERSION=3.3.1
ENV HADOOP_HOME=/opt/hadoop
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}

RUN wget --no-verbose -O hadoop.tgz "https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz" \
  && mkdir -p /opt/hadoop \
  && tar -xf hadoop.tgz -C /opt/hadoop --strip-components=1 \
  && rm hadoop.tgz

RUN mkdir /workspace

FROM builder as hadoop

WORKDIR /workspace

ENTRYPOINT ["tail", "-f", "/dev/null"]