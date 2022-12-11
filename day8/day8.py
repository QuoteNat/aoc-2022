import timeit
start = timeit.default_timer()

inputs = list()
with open("input", "r") as file:
    inputs = file.readlines()

# input cleaning
for i in range(len(inputs)):
    inputs[i] = inputs[i].replace("\n", "")

forest = list()

# Convert inputs to 2d array of ints
for line in inputs:
    row = list()
    for char in line:
        row.append(int(char))
    forest.append(row)

count = 0
# Add edges to count (len of row * 2) + (number of rows - 2) * 2
count = count + len(forest[0])*2 + (len(forest)-2) * 2


tmax = forest[0]
lmax = list()
for i in range(len(forest)):
    lmax.append(forest[i][0])

# Iterate through rows, not including edge rows
for i in range(1, len(forest)-1):
    # Iterate through columns, not including edge columns
    for j in range(1, len(forest[i])-1):
        curTree = forest[i][j]

        # get max to right of curTree
        rmax = max(forest[i][j+1:])

        # get max below curTree
        bmax = 0
        for n in range(i+1, len(forest)):
            if forest[n][j] > bmax:
                bmax = forest[n][j]
        # If current tree is greater than the max of trees up, down, left, or right of it, it's visible
        if curTree > lmax[i] or curTree > rmax or curTree > tmax[j] or curTree > bmax:
            count = count + 1
        
        # Update lmax and tmax if the curTree is a new max
        if curTree > lmax[i]:
            lmax[i] = curTree
        
        if forest[i][j] > tmax[j]:
            tmax[j] = curTree

print("Visible trees outside grid:", count)
stop = timeit.default_timer()
print('Runtime part 1:', stop - start, 'seconds')
# ----------------PART 2---------------
start = timeit.default_timer()

bestScore = 0
# We can skip edges, as the score for any edge will be 0 due to multiplication
for i in range(1, len(forest)-1):
    for j in range(1, len(forest[i])-1):
        curTree = forest[i][j]
        # print(i, j)
        # Calculate nScore
        nmaxFound = False
        countN = 0
        while nmaxFound == False and i - (countN + 1) >= 0:
            seenTree = forest[i - (countN + 1)][j]
            # if seenTree < curTree then increase countN by 1
            if seenTree < curTree:
                countN = countN + 1
            # if seenTree is taller, then stop counting
            else:
                countN = countN + 1
                nmaxFound = True

        # Calculate eScore
        emaxFound = False
        countE = 0
        while emaxFound == False and j + countE + 1 < len(forest[i]):
            seenTree = forest[i][j + (countE + 1)]
            # if seenTree < curTree then increase countN by 1
            if seenTree < curTree:
                countE = countE + 1
            # if seenTree is the same height, increase countN by 1 and stop counting
            else:
                countE = countE + 1
                emaxFound = True

        # Calculate sScore
        smaxFound = False
        countS = 0
        while smaxFound == False and i + countS + 1 < len(forest):
            seenTree = forest[i + (countS + 1)][j]
            # if seenTree < curTree then increase countN by 1
            if seenTree < curTree:
                countS = countS + 1
            # if seenTree is the same height, increase countN by 1 and stop counting
            else:
                countS = countS + 1
                smaxFound = True


        # Calculate nscore
        wmaxFound = False
        countW = 0
        while wmaxFound == False and j - (countW + 1) >= 0:
            seenTree = forest[i][j - (countW + 1)]
            # if seenTree < curTree then increase countN by 1
            if seenTree < curTree:
                countW = countW + 1
            # if seenTree is the same height, increase countN by 1 and stop counting
            else:
                countW = countW + 1
                wmaxFound = True


        # Calculate score
        # print(countN, countE, countS, countW)
        score = countN * countE * countS * countW
        if score > bestScore:
            bestScore = score

print("Best score:", bestScore)
stop = timeit.default_timer()
print('Runtime part 2:', stop - start, 'seconds')