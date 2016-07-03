#!/usr/bin/env python

import requests
import base64
import json
from array import array
from struct import pack
from sys import byteorder
from pprint import pprint
import urllib
import getopt, sys
import os

try:
  opts, args = getopt.getopt(sys.argv[1:], "fgsbt:v", ["file=", "group=","title=","body="])
except getopt.GetoptError as err:
  # print help information and exit:
  print str(err)  # will print something like "option -a not recognized"
  usage()
  sys.exit(2)
output = None
verbose = False
dont_notify = False
body = ''
title = ''
for o, a in opts:
  if o == "-v":
    verbose = True
  elif o in ("-f", "--file"):
    source_file = a
  elif o in ("-g", "--group"):
    group = a
  elif o in ("-s"):
    dont_notify = True
  elif o in ("-b", "--body"):
    body = a 
  elif o in ("-t", "--title"):
    title = a 
  else:
    assert False, "unhandled option"

with open(os.path.dirname(os.path.abspath(__file__)) + '/config.json') as config_file:    
    config = json.load(config_file)

try:
  t = group
except:
  print "No Group ID Passed"

try:
  t = source_file
except:
  print "No File passed"
  

  
try:
  t = config['hostname']
except:
    print "unable to load valid config file. Missing Host Name"
    exit(1)   
    
try: 
  t = config['api_endpoint']
except:
    print "unable to load valid config file. Missing API End Point"
    exit(1)  
try:
  t=config['key']
except:
    print "unable to load valid config file. Missing Application Key"
    exit(1)  
        
print source_file      
try:
  with open(source_file, "rb") as audio_file:
      encoded_audio_file = base64.b64encode(audio_file.read())  
except:
  print "unable to load Audio File"
  exit(1)
    

url = config['hostname'] + config['api_endpoint']

payload = dict()
payload['message'] = dict()
payload['message']['group_id'] = group
payload['message']['audio_file'] = encoded_audio_file
payload['message']['dont_notify'] = dont_notify
payload['message']['title'] = title
payload['message']['body'] = body

try:
  response = requests.post(url, json=payload)
except: 
  print "Unable to reach Server"
  exit(1)
  
  
if response.status_code == requests.codes.ok:
  print "Valid response"
  exit(0)
else:
  print "Error in response: " + str(response.status_code)
  exit(1)
  
