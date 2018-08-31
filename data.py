#! /usr/bin/env python
# Author : jyoti.bhanot30@gmail.com

import os
import boto3
import botocore
import re
import collections
import urllib3

# to supress warnings into console
urllib3.disable_warnings()

# to get boto3 session using aws credentials
def get_session(aws_access_key_id, aws_secret_access_key):
  session = boto3.Session(
      aws_access_key_id = aws_access_key_id.strip('\n'),
      aws_secret_access_key = aws_secret_access_key.strip('\n'),
  )
  return session

# this function downloads files from s3 bucket.
def download_files(files, bucket, aws_access_key_id, aws_secret_access_key):
  session = get_session(aws_access_key_id, aws_secret_access_key)
  s3 = session.resource('s3')
  for file in files:
     try:
         s3.Bucket(bucket).download_file(file, os.path.basename(file))
     except botocore.exceptions.ClientError as e:
         if e.response['Error']['Code'] == "404":
             print("The object does not exist.")
         else:
             raise

# this function returns top5 most frequent words
def get_top5(filename):
  with open(filename) as f:
      text = f.read()
  text = text.lower()
  words = re.findall(r'\w+', text)
  counts = collections.Counter(words)
  top5 = counts.most_common(5)
  return top5

# to read aws credentials from file
def get_creds_from_file(path):
  with open(path, 'r') as creds:
    credentials = creds.readlines()
  creds.close()
  return credentials

def main():
  aws_credentials_file = 'aws_credentials'
  credentials = get_creds_from_file(aws_credentials_file)
  files = ['task.txt'] # For multiple files
  bucket = 'datagrokr-assessment'
  download_files(files, bucket, credentials[0], credentials[1])
  for filename in files:
    top5 = get_top5(filename)
    for word in top5:
      print word[0]

if __name__ == '__main__':
  main()
