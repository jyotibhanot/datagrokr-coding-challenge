# Base Ubuntu image with base packages
FROM jyotibhanot30/ubuntu-base:latest

# Install dependencies
RUN apt-get update && \ 
    apt-get install python-pip -y && \
    pip install boto3 

# Present working directory
WORKDIR /opt

# Copy aws credentials file
COPY aws_credentials . 

# Copy python code
COPY data.py .

# pid 1
CMD tail -f /dev/null
