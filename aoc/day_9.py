

a = [10,13,16,21,30,45] 

dic = {}

def next_val():
    def recursion(i, line, new_line, layer):
        if sum(line) == 0:
            return layer
        
        dic[layer] = line[-1]
        for i in range(len(line)-1):
            new_line.append(line[i+1] - line[i])
        
        return recursion(0, new_line, [], layer + 1)

        
    
    return recursion(0,a, [], 0)

layer = next_val()
print (dic, layer)

prev = dic[layer-1]
for i in range(layer-2,-1,-1):
    prev = dic[i] + prev
print (prev)

    
