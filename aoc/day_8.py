import sys

def parse_line(line):
    key, value = line.strip().split(' = ')
    return key, value

# Read the content of the file and parse each line
with open('day_8_data.txt', 'r') as file:
    lines = file.readlines()

with open('day_8_data_p2.txt', 'r') as file:
    path = file.readlines()[0]

# Create the dictionary from parsed lines
my_dict = {}
for key, value in map(parse_line, lines):
    print (key, value)
    print (value.strip("()").split(", "))
    my_dict[key] = value.strip("()").split(", ")


class mySolution:
    def parse_tree(self, my_dict, path):
        sys.setrecursionlimit(15000)
        self.count = 0
        def dfs(node, p, i):
            if node == 'ZZZ':
                return 
            self.count += 1
            if i >= len(p):
                i = 0
            
            if p[i] == 'L':
                dfs(my_dict[node][0], p, i+1)
            else:
                # path == R
                dfs(my_dict[node][1], p, i+1)
        dfs('AAA', path, 0)
        return self.count
mys = mySolution()
print ("ans: ", mys.parse_tree(my_dict, path))