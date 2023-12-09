# Solution 1
f = open("test_data.txt").read().strip()
seqs = [[int(x) for x in l.split()] for l in f.split('\n')]

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

# Solution 2 is simply reversing the seq before recursive call.