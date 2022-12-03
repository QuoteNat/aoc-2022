# Winning pairs
MATCH_PAIRS = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

WIN_PAIRS = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

LOSE_PAIRS = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

SHAPE_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

lines = list()
with open('input', 'r') as input:
    lines = input.readlines()

pairs = list()

for line in lines:
    line = line.replace("\n", "")
    pairs.append(tuple(line.split(" ")))

score_sum = 0
for pair in pairs:
    score_sum = score_sum + SHAPE_SCORES[pair[1]]

    if MATCH_PAIRS[pair[0]] == pair[1]:
        score_sum = score_sum + 3
    elif WIN_PAIRS[pair[0]] == pair[1]:
        score_sum = score_sum + 6

print("Fake score sum: {}".format(score_sum))

# Part 2
real_score_sum = 0

for pair in pairs:
    if pair[1] == "X":
        # print("{} + {}".format(0, SHAPE_SCORES[LOSE_PAIRS[pair[0]]]))
        real_score_sum = real_score_sum + SHAPE_SCORES[LOSE_PAIRS[pair[0]]]
    elif pair[1] == "Y":
        # print("{} + {}".format(3, SHAPE_SCORES[MATCH_PAIRS[pair[0]]]))
        real_score_sum = real_score_sum + 3
        real_score_sum = real_score_sum + SHAPE_SCORES[MATCH_PAIRS[pair[0]]]
    else:
        real_score_sum = real_score_sum + 6
        real_score_sum = real_score_sum + SHAPE_SCORES[WIN_PAIRS[pair[0]]]

print("Real score sum: {}".format(real_score_sum))