import re

list_nums = []
with open('readpls.txt') as f:
    for line in f:
        line = line.strip()
        nums = re.compile('[,] ').split(line)
        for value in nums:
            list_nums.append(value)

print(list_nums)