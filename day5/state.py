from collections import deque

# Problem state class representing the current state of the problem
class State:
    # Take a problem input as an array of strings
    def __init__(self, input):
        # Get number of columns/stacks
        rawColumns = input[len(input)-1].split(" ")
        columns = list()
        for i in rawColumns:
            if i != '':
                columns.append(i)
        colNum = int(columns[len(columns)-1])

        # Create stacks member
        self.stacks = list()
        for i in range(colNum):
            self.stacks.append(deque())

        # Iterate backwards through the inputs lines after the columns
        for i in range(len(input)-2, -1, -1):
            line = input[i]
            # Step through
            for j in range(1, len(line), 4):
                if line[j] != " ":
                    self.stacks[int((j-1)/4)].append(line[j])
