#!/usr/bin/env python3

import json
import os, sys

from urllib.parse import urlencode
from urllib.request import Request, urlopen

def main():
  if len(sys.argv) < 2:
    print('Usage: ./gcs_md5.py <bucket-name>')
    sys.exit(1)

  bucket = sys.argv[1]
  access_token = os.popen('gcloud auth print-access-token').read()[:-1]

  url = 'https://www.googleapis.com/storage/v1/b/%s/o' % bucket
  headers = {
    'Authorization': 'Bearer %s' % access_token,
  }
  items = []
  page_token = ''
  while True:
    params = urlencode({
      'fields': 'nextPageToken,items(name,md5Hash)',
      'pageToken': page_token,
    })
    res = urlopen(Request(url + '?' + params, headers=headers))
    res = json.loads(res.read().decode("utf-8"))
    items.extend(res['items'])
    if 'nextPageToken' not in res:
      break
    page_token = res['nextPageToken']
  print(json.dumps({
    'items': items,
  }, indent=2))

if __name__ == '__main__':
    main()
