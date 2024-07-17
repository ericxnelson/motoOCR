# motoOCR

This repo has a dockerfile to manage dependencies and has a few scripts to detect words/numbers using OCR and tag the image metadata "Keywords" field with results if any are found

- scripts/test.py
  - process file manually and save a result image with boxed results

- scripts/findOCR.py
  - process image as sys.argv[1] and tag it with any found strings

- scripts/processDir.sh
  - iterate through all jpg files in a directory and tag with any results found


## Quickstart

- build/run docker image (requires root and working docker)
```motoOCR$ sudo docker build -t motofoto:latest .
[+] Building 197.6s (11/11) FINISHED                                                                                                               docker:default
 => [internal] load .dockerignore                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                              0.0s
 => [internal] load build definition from Dockerfile                                                                                                         0.0s
 => => transferring dockerfile: 290B                                                                                                                         0.0s
 => [internal] load metadata for docker.io/library/ubuntu:22.04                                                                                              0.0s
 => [internal] load build context                                                                                                                            0.0s
 => => transferring context: 1.13kB                                                                                                                          0.0s
 => [1/6] FROM docker.io/library/ubuntu:22.04                                                                                                                0.0s
 => CACHED [2/6] RUN apt -y update && apt -y upgrade                                                                                                         0.0s
 => CACHED [3/6] RUN apt -y install python3-pip vim tmux imagemagick ffmpeg libsm6 libxext6                                                                  0.0s
 => [4/6] RUN pip3 install paddleocr paddlepaddle paddlepaddle-gpu exif rasterio                                                                           177.6s
 => [5/6] RUN mkdir -p /opt/code                                                                                                                             0.4s
 => [6/6] COPY scripts /opt/code                                                                                                                             0.1s 
 => exporting to image                                                                                                                                      19.5s 
 => => exporting layers                                                                                                                                     19.5s 
 => => writing image sha256:19513d0dea0c4455e1a2930aebcdaddbf9c1d30e02b8e4ea8f4e375fb6a03f64                                                                 0.0s 
 => => naming to docker.io/library/motofoto:latest                                                                                                           0.0s 
```

- run script to process jpgs in dir


```motoOCR$ sudo docker run -v /mnt:/mnt -it motofoto:latest bash
root@36abc9bcede1:/# 
root@36abc9bcede1:~# cd /opt/code/ 
root@36abc9bcede1:/opt/code# ls
findOCR.py  processDir.sh  test.py
root@36abc9bcede1:/opt/code# bash processDir.sh /mnt/DCIM/some_dir_of_jpgs
```
