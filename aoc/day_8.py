def parse_line(line):
    key, value = line.strip().split(' = ')
    return key, value

# Read the content of the file and parse each line
with open('day_8_data.txt', 'r') as file:
    lines = file.readlines()

# Create the dictionary from parsed lines
my_dict = {}
for key, value in map(parse_line, lines):
    print (key, value)
    print (value.strip("()").split(", "))
    my_dict[key] = value.strip("()").split(", ")
print (my_dict)