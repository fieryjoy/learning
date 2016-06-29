FROM ubuntu:16.04
RUN \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y python3.5 python3-pip curl devscripts build-essential libncurses5 git debhelper libgeos-dev libgdal-dev python3-gdal libspatialindex-dev && \
apt-get -y autoremove && \
apt-get -y clean
