# Returns true if either range fully contains the other
# param: range1 array of type [min, max]
# param: range2 array of type [min, max]
def contains(range1, range2):
    # If range1[min] is less than or equal to range2[min] and
    # range1[max] is greater than or equal to range2[max]
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        return True
    # else if vice versa of above is true (range 2 contains range 1)
    elif range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    else:
        return False

# Returns true if the ranges intersect each other
# param: range1 array of type [min, max]
# param: range2 array of type [min, max]
def intersects(range1, range2):
    # if range1[min] is greater than range2[max] or range1[max] is less than
    if range1[0] > range2[1] or range1[1] < range2[0]:
        return False
    else:
        return True

# Converts a range of strings to ints
def rangeToINT(range):
    return [int(range[0]), int(range[1])]

inputs = list()
with open("input", "r") as file:
    inputs = file.readlines()

# input cleaning
for i in range(len(inputs)):
    inputs[i] = inputs[i].replace("\n", "")

# iterate through range pairs
count = 0 # Number of assignment pairs where one range contains the other
countIntersect = 0
for pair in inputs:
    # Convert the input line into two lists representing the range as ints
    splitPair = pair.split(",")
    range1 = rangeToINT(splitPair[0].split("-"))
    range2 = rangeToINT(splitPair[1].split("-"))
    
    if contains(range1, range2):
        count = count + 1
    if intersects(range1, range2):
        countIntersect = countIntersect + 1

print("Number of pairs where one range contains the other: {}".format(count))
print("Number of pairs where an intersection occurs: {}".format(countIntersect))
