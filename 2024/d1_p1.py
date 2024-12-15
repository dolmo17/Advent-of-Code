import re

total = 0
right = []
left = []

# parse numbers from the input file
f = open("input.txt", 'r')
reg = "\d+"
vals = re.findall(reg, f.read())
f.close()


# assemble each list
left = [int(val) for val in vals[::2]]
right = [int (val) for val in vals[1::2]]

# bubble sort each list
n = len(left)

for i in range(n):
    for j in range(0, n - i - 1):
        if left[j] > left[j + 1]:
            swp = left[j]
            left[j] = left[j + 1]
            left[j + 1] = swp
            
        if right[j] > right[j + 1]:
            swp = right[j]
            right[j] = right[j + 1]
            right[j + 1] = swp

# at each index, add the values in the left and right lists together, add to total
for i in range(n):
    total += abs(left[i] - right[i])
    
print(total)