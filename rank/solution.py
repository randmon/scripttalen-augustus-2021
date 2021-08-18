import json

with open('input.json') as input:
    data = json.loads(input.read())

data = sorted(data, key=lambda k: k['score'], reverse=True)
i = 1
for d in data:
    print (f"{i} {d['name']}")
    i += 1
#934ea76e49e236e21c3c302cce