import sys

with open(sys.argv[1], 'r', encoding='utf8') as file:
    contents = []
    for line in file:
        contents.append(list(map(int,line.strip())))