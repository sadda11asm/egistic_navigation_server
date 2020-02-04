FROM geographica/gdal2:2.4.3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /
COPY req_init.txt ./
#RUN pip install --upgrade pip
RUN apt-get -y install libcurl4-openssl-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
	python3-setuptools \
	libzmq3-dev \
	libevent-dev \
	curl \
	python3-pycurl \
	unzip \
    file \
    wget \
    swig \
    # for sen2three:
    libopenjp2-7
RUN pip3 install wheel
RUN pip3 install lgblkb-navigation
RUN pip3 install -r req_init.txt
RUN rm req_init.txt

COPY . /app
WORKDIR /app
