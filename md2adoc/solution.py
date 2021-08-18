import re

with open('input.md') as input:
    for line in input:
        heading = re.match("(#+)", line)
        if heading:
            line = re.sub(heading.group(1), "="*len(heading.group(1)), line)
        else:
            bullet = re.match(r"((  )+)\*", line)
            if bullet:
                amount = int(len(bullet.group(1))/2)
                line = re.sub(bullet.group(1), "*" * amount, line)
        print(line[:-1])
#5c1a5bf4bce133b53ecfab38b6