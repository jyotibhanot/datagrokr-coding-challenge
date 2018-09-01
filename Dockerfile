# Base Ubuntu image with base packages
FROM python:2.7-alpine

# Install dependencies
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install boto3 \
  && rm -rf /var/cache/apk/*

# Change home directory
WORKDIR /home

# Copy aws credentials file
COPY aws_credentials . 

# Copy python code
COPY data.py .

# pid 1
CMD tail -f /dev/null
