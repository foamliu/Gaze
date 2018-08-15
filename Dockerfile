FROM base/archlinux
MAINTAINER Peisheng Wang <115681033@qq.com>
RUN pacman -Syu --noconfirm
RUN pacman -S opencv gtk3 hdf5 python-numpy --noconfirm
RUN pacman -S gstreamer --noconfirm
RUN pacman -S python-pip --noconfirm
RUN pip install gaze
RUN pacman -S unzip --noconfirm
RUN mkdir -p /usr/src/gaze
COPY temp/pkg.zip /usr/src/gaze
WORKDIR /usr/src/gaze
RUN unzip pkg.zip
EXPOSE 80
CMD [ "python", "app.py" ]