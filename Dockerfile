FROM python:3.8

COPY . /opt

RUN cd /opt/overture-python-sdk && python setup.py install

