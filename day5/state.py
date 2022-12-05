from collections import deque
import re

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
            # Add each element of a line to it's respective stacks
            for j in range(1, len(line), 4):
                # Skip if there's a space, which means there is no element at this position
                if line[j] != " ":
                    self.stacks[int((j-1)/4)].append(line[j])

    # Move items from one stack to another
    def move(self, command):
        # Quantity of items to move
        commandList = command.split(" ")
        # Quantity of items to move
        quant = int(commandList[1])
        # source and destination indexes
        source = int(commandList[3])-1
        dest = int(commandList[5])-1

        for _ in range(quant):
            # Pop rightmost element of source and append/push it to dest
            self.stacks[dest].append(self.stacks[source].pop())
        
    
    # Return a string containing the top elements of each stack in order
    def getTops(self):
        returnString = ""
        for stack in self.stacks:
            returnString = returnString + stack[len(stack)-1]
        return returnString
