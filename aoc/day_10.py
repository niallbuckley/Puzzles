def load_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return file_content
map = []
for line in load_file("day_10_data.txt").split():
    map.append(list(line))

print (map)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'S':
            start = (i,j)
queue = []
queue.append(start)
print (queue)
level = -1
seen = set()
seen.add(start)
while queue:
    level += 1
    print ("new level")
    for i in range(len(queue)):
        n_r, n_c = queue.pop(0)
        print (n_r, n_c)
        if (n_r < len(map) and n_r >= 0) and (n_c < len(map[0]) and n_c >= 0):
            print ("here")
            if map[n_r][n_c] == 'S':
                neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
            elif map[n_r][n_c] == 'F':
                neighbors = [(0,1), (1,0)]
            elif map[n_r][n_c] == '-':
                neighbors = [(0,1), (0,-1)]
            elif map[n_r][n_c] == '|':
                neighbors = [(1,0), (-1, 0)]
            elif map[n_r][n_c] == '|':
                neighbors = [(1,0), (-1, 0)]
            elif map[n_r][n_c] == 'L':
                neighbors = [(0,1), (-1,0)]
            elif map[n_r][n_c] == '7':
                neighbors = [(0,-1), (1,0)]
            elif map[n_r][n_c] == 'J':
                neighbors = [(-1,0), (0,-1)]
            else:
                print ("No neighs", map[n_r][n_c])
                neighbors = []
                continue
        else:
            print ("Out of range")
            continue
        for neigh in neighbors:
            new_node = n_r + neigh[0], n_c + neigh[1]
            if new_node not in seen:
                queue.append(new_node)
                seen.add(new_node)

print ("ans", level)