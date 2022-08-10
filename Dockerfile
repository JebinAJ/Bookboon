FROM ubuntu:18.04   
ADD bookboon.sh /
RUN bash -c "/bootstrap.sh"