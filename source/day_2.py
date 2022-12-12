import pathlib

# Part 1
path = pathlib.Path.cwd() / 'data' / 'day_2'
problem_text = path.read_text()

pairs = problem_text.split('\n')

# part_1

first_hand = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

second_hand = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

hand_score = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

# for testing function
pair = pairs[0]


def calculate_score(pair: str):
    first_hand_actual = first_hand[pair[0]]
    second_hand_actual = second_hand[pair[2]]

    losing_hand_pairs = [
        ('paper', 'rock'),
        ('scissors', 'paper'),
        ('rock', 'scissors')
    ]

    second_hand_score = hand_score[second_hand_actual]

    if first_hand_actual == second_hand_actual:
        match_score = 3
    elif (first_hand_actual, second_hand_actual) in losing_hand_pairs:
        match_score = 0
    else:
        match_score = 6

    return match_score + second_hand_score


all_scores = [
    calculate_score(pair)
    for pair
    in pairs
]

sum(all_scores)

# part 2

first_hands_with_hand_2_results = {
    'rock': {
        'draw': 'rock',
        'win': 'paper',
        'lose': 'scissors',
    },
    'paper': {
        'lose': 'rock',
        'draw': 'paper',
        'win': 'scissors',
    },
    'scissors': {
        'win': 'rock',
        'lose': 'paper',
        'draw': 'scissors',
    },
}

hand_result = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}


def calculate_score_part_2(pair: str):
    first_hand_actual = first_hand[pair[0]]
    result = hand_result[pair[2]]

    second_hand_actual = first_hands_with_hand_2_results[first_hand_actual][result]

    if result == 'win':
        match_score = 6
    elif result == 'draw':
        match_score = 3
    else:
        match_score = 0

    return match_score + hand_score[second_hand_actual]


all_scores_part_2 = [
    calculate_score_part_2(pair)
    for pair
    in pairs
]

sum(all_scores_part_2)
