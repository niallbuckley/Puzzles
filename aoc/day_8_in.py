from collections import namedtuple
#from aql import load_file

def load_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

LR = namedtuple("LR", "L R")

inp = load_file("day_8_data.txt")

instructions, raw_nodes = inp.split("\n\n")

nodes = {}
for node in raw_nodes.splitlines():
    node, lr = node.split(' = ')
    left, right = lr.strip()[1:-1].split(", ")
    nodes[node] = LR(left, right)

print (nodes)

