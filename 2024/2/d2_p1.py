import re

safes = 0

# parse reports from the input file
reg = "\d+"
with open("input.txt", "r") as f:
    for line in f:
        nums = re.findall(reg, line) # get all numbers in the line
        levels = [int(val) for val in nums] # convert the numbers to ints

        isIncr = False
        isDecr = False
        isSafe = True
        for i, level in enumerate(levels): # process each report
            if i + 1 != len(levels): # make sure we don't go out of bounds
                if level < levels[i + 1]:
                    if isDecr:
                        isSafe = False # decreasing after increase, unsafe
                    isIncr = True
                    diff = levels[i + 1] - level

                elif level > levels[i + 1]:
                    if isIncr:
                        isSafe = False # increase after decrease, unsafe
                    isDecr = True
                    diff = level - levels[i + 1]

                else:
                    isSafe = False # neither increasing nor decreasing, thus unsafe

            
            if diff > 3:
                isSafe = False # difference greater than 3, unsafe

        if isSafe:
            safes += 1 # otherwise, the report is safe!

f.close()

print(safes)
