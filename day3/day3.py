# Make the priority list
priority_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
inputs = list()
with open("input", "r") as file:
    inputs = file.readlines()

# input cleaning
for i in range(len(inputs)):
    inputs[i] = inputs[i].replace("\n", "")

file.close()

match_list = list()

for input in inputs:
    # Split into two comparments
    middle = int(len(input)/2)
    compartment1 = input[0:middle]
    compartment2 = input[middle:]

    # Set to prevent duplicates per rucksack
    compartment_set = set()
    for char in compartment1:
        if char in compartment2:
            compartment_set.add(char)
    
    # Add compartment_set characters to match_list, which does allow duplicates
    for char in compartment_set:
        match_list.append(char)

priority_sums = 0
for item in match_list:
    # Priorities are just the index in the priority_list + 1
    priority_sums = priority_sums + priority_list.find(item) + 1

print("Part 1: {}".format(priority_sums))

# ----------PART 2-------------
group_sums = 0

# Hope you like multiplication :)
for i in range(int(len(inputs)/3)):
    baseIndex = i * 3
    groupMember1 = inputs[baseIndex]
    groupMember2 = inputs[baseIndex+1]
    groupMember3 = inputs[baseIndex+2]
    
    # loop through group member 1 until a match is found in all 3
    found = False
    j = 0
    while not found and j < len(groupMember1):
        char = groupMember1[j]
        if char in groupMember2 and char in groupMember3:
            group_sums = group_sums + priority_list.find(char) + 1
            found = True
        j = j + 1

print("Part 2: {}".format(group_sums))