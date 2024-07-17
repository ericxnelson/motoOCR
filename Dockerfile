FROM ubuntu:22.04

RUN apt -y update && apt -y upgrade

RUN apt -y install python3-pip vim tmux imagemagick ffmpeg libsm6 libxext6

RUN pip3 install paddleocr paddlepaddle paddlepaddle-gpu exif rasterio pyexiftool

RUN mkdir -p /opt/code

COPY scripts /opt/code
