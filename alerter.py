import requests
import base64
import json
from array import array
from struct import pack
from sys import byteorder
import copy




url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
response = requests.get(url, data=data)
