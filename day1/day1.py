# open input file

calorie_sums = list()
temp_sum = 0
lines = list()
with open('input', 'r') as input:
    lines = input.readlines()

for line in lines:
    if line == "\n":
        calorie_sums.append(temp_sum)
        temp_sum = 0
    else:
        temp_sum = temp_sum + int(line)

print(max(calorie_sums))

# Part 2
calorie_sums.sort(reverse=True)
print(calorie_sums[0] + calorie_sums[1] + calorie_sums[2])