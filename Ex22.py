name_count_dict = {}


with open('nameslist.txt', 'r') as open_file:
    line = open_file.readline().rstrip('\n')
    while line:
        name_count_dict[line] = name_count_dict.get(line, 0) + 1
        line = open_file.readline().rstrip('\n')

print(name_count_dict)