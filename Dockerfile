FROM base/archlinux
MAINTAINER Peisheng Wang <115681033@qq.com>
RUN pacman -Syu
RUN pacman -S opencv
RUN pacman -S gstreamer
RUN pacman -S python-numpy
RUN pacman -S python-pip
RUN pip install gaze
RUN pacman -S unzip
RUN mkdir -p /usr/src/gaze
COPY temp/pkg.zip /usr/src/gaze
WORKDIR /usr/src/gaze
RUN unzip pkg.zip
EXPOSE 80
CMD [ "python", "app.py" ]