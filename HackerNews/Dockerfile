# Using official python image as base
from python:3

RUN pip install urllib3 certifi

ADD hn.py /docker/hn.py

ENTRYPOINT python /docker/hn.py
