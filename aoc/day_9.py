# Solution 1
f = open("test_data.txt").read().strip()
seqs = [[int(x) for x in l.split()] for l in f.split('\n')]

dic = {}

def next_val(seq):
    def recursion(i, line, new_line, layer):
        if sum(line) == 0:
            return layer
        
        dic[layer] = line[-1]
        for i in range(len(line)-1):
            new_line.append(line[i+1] - line[i])
        
        return recursion(0, new_line, [], layer + 1)

        
    
    return recursion(0,seq, [], 0)

ans = 0
for seq in seqs:
    layer = next_val(seq)
    prev = dic[layer-1]
    for i in range(layer-2,-1,-1):
        prev = dic[i] + prev
    ans += prev
print ("ans:", ans)

# Solution 2 is simply reversing the seq before recursive call.
    
## in-memory storage rather than dictionary

def get_next_in_seq(sq):
    if not any(sq):
        return 0

    diffs = []
    for i in range(len(sq)-1):
        diffs.append(sq[i+1] - sq[i])
        
    return sq[-1] + get_next_in_seq(diffs)

result = 0
for seq in seqs:
    result += get_next_in_seq(seq)
print("ans " + str(result))