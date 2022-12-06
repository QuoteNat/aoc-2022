# # Input string
input = ''
with open("input", "r") as file:
    input = file.readline()

file.close()

# Check in the range of 4 to the length of the input (assume answer will be found before \n)
for i in range(4, len(input)):
    test_set = {input[i-3]}
    test_set.add(input[i-2])
    test_set.add(input[i-1])
    test_set.add(input[i])
    # When the set is of length 4 (no matches found)
    if (len(test_set) == 4):
        # Output processed chars (index+1)
        print("First start of packet:")
        print(i+1)
        break

#---------------------part 2------------------
for i in range(14, len(input)):
    test_set = {input[i]}
    for j in range(1, 14):
        test_set.add(input[i-j])
    # When the set is of length 4 (no matches found)
    if (len(test_set) == 14):
        # Output processed chars (index+1)
        print("First start of message:")
        print(i+1)
        break