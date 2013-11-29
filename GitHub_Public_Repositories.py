import urllib2
import re
import sys
import json
import csv
from collections import defaultdict
from random import random

auth_token = '' # insert your Personal Auth Token here
iterations = 3000

req = urllib2.Request('https://api.github.com/repositories')
req.add_header('Authorization', 'token %s' % auth_token)

response = urllib2.urlopen(req)

data = json.loads(response.read())

repo_names = []
repo_desc = []

for i in range(iterations):
    print i


    for repo in data:
        try:
            repo_names.append(repo['name'].replace("-"," ").replace("_"," ").encode('utf-8').strip())
            repo_desc.append(repo['description'].encode('utf-8').strip())
        except:
            pass
    try:
        req = urllib2.Request('https://api.github.com/repositories?since=%s' % data[len(data)-1]["id"])
        req.add_header('Authorization', 'token %s' % auth_token)
        response = urllib2.urlopen(req)
        data = json.loads(response.read())
    except:
        pass

print "done!"

with open('github_repo_names.txt', 'w') as fp:
    a = csv.writer(fp, delimiter='\n')
    a.writerows([repo_names,])

with open('github_repo_desc.txt', 'w') as fp:
    a = csv.writer(fp, delimiter='\n')
    a.writerows([repo_desc,])






