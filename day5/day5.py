from state import State

inputs = list()
with open("example", "r") as file:
    inputs = file.readlines()

# input cleaning
for i in range(len(inputs)):
    inputs[i] = inputs[i].replace("\n", "")

# for line in inputs:
#     print(line)

# Pass in initial state information to the state constructor
init_state = list()
for i in range(inputs.index("")):
    init_state.append(inputs[i])

state = State(init_state)

# Pass in movement commands to state
for i in range(inputs.index("")+1, len(inputs)):
    state.move(inputs[i])