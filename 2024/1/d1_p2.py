import re

sim = 0
right = []
left = []
rightCounts = {}

# parse numbers from the input file
f = open("input.txt", 'r')
reg = "\d+"
vals = re.findall(reg, f.read())
f.close()

# assemble each list
left = [int(val) for val in vals[::2]]
right = [int (val) for val in vals[1::2]]

# get the count of each number in the right list, add it to the dictionary
for num in right:
    rightCounts[num] = rightCounts.get(num, 0) + 1

# for each num in the left list, increment the similarity score by
# the num's occurrences in the right list
for num in left:
    sim += num * rightCounts.get(num, 0)

print(sim)