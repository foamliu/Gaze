FROM ubuntu:16.04
MAINTAINER Peisheng Wang <115681033@qq.com>
RUN apt-get update -y
RUN apt-get -y install python3-pip
RUN pip3 install gaze
RUN apt-get install unzip
RUN mkdir -p /usr/src/gaze
COPY temp/pkg.zip /usr/src/gaze
WORKDIR /usr/src/gaze
CMD [ "unzip", "pkg.zip" ]
CMD [ "python3", "app.py" ]