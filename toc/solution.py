import re

with open('input.asciidoc') as input:
    file = input.read()

headings = re.findall(r'\[\#(.*)\]\n(=+) (.*)', file)
for h in headings:
    id = h[0]
    k = '*' *len(h[1])
    title = h[2]
    print(f"{k} <<{id},{title}>>")
#790741be97ceb64a5637d35fc9