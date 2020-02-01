FROM python:3.7-stretch
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /
COPY req_init.txt ./
#RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r req_init.txt
RUN rm req_init.txt

COPY . /app
WORKDIR /app
