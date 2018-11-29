FROM ubuntu:16.04
MAINTAINER Jingyi Zhu <t-jinzhu@microsoft.com>
# Install gstreamer and opencv dependencies
RUN \ 
    apt-get update && apt-get upgrade -y && \
    apt-get install -y python3-pip \
        python3 \
        python3-dev && \
    pip3 install numpy
RUN \
    apt-get install -y libgstreamer1.0-0 \
            gstreamer1.0-plugins-base \
            gstreamer1.0-plugins-good \
            gstreamer1.0-plugins-bad \
            gstreamer1.0-plugins-ugly \
            gstreamer1.0-libav \
            gstreamer1.0-doc \
            gstreamer1.0-tools \
            libgstreamer1.0-dev \
            libgstreamer-plugins-base1.0-dev && \
    apt-get install -y \
        wget \
        unzip \
        libtbb2 \
        libtbb-dev && \
    apt-get install -y \
        build-essential \
        cmake \
        git \
        pkg-config \
        libjpeg8-dev \
        #libtiff4-dev \
        libjasper-dev \
        libpng12-dev \
        libgtk2.0-dev \
        libavcodec-dev \
        libavformat-dev \
        libswscale-dev \
        libv4l-dev \
        libatlas-base-dev \
        gfortran \
        libhdf5-dev && \
    apt-get autoclean && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#RUN \
#    sudo -E add-apt-repository -y ppa:george-edison55/cmake-3.5.x && \
#    sudo -E apt-get update && \
#    sudo apt-get install cmake

RUN apt-get install gcc
RUN git clone https://github.com/opencv/opencv.git
RUN \
    cd opencv && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_C_EXAMPLES=OFF \
        #-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
        -D BUILD_opencv_python3=ON \
        -D WITH_GSTREAMER=ON \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D BUILD_EXAMPLES=ON .. && \
    make && \
    make install

ADD ../Gaze/ /
RUN cd Gaze
EXPOSE 5001
CMD [ "python", "./server.py" ]

# Download OpenCV 3.2.0 and install
#RUN \
#    cd ~ && \
#    wget https://github.com/Itseez/opencv/archive/3.2.0.zip && \
#    unzip 3.2.0.zip && \
#    mv ~/opencv-3.2.0/ ~/opencv/ && \
#    rm -rf ~/3.2.0.zip && \
#    cd /root/opencv && \
#    mkdir build && \
#    cd build && \
#    cmake -D CMAKE_BUILD_TYPE=RELEASE \
#        -D CMAKE_INSTALL_PREFIX=/usr/local \
#        -D INSTALL_C_EXAMPLES=OFF \
#        -D INSTALL_PYTHON_EXAMPLES=ON \
#        -D BUILD_EXAMPLES=ON .. && \
#    cd ~/opencv/build && \
#    make -j $(nproc) && \
#    make install && \
#    ldconfig
