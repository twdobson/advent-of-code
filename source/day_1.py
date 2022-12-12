import pathlib
from typing import List

# Part 1
path = pathlib.Path.cwd() / 'data' / 'problem_1_1'
problem_text = path.read_text()

problem_text_split = problem_text.split('\n\n')


def sum_list_of_string(list_of_strings: List[str]):
    return sum(
        [
            int(string)
            for string
            in list_of_strings
        ]
    )


per_elf = [
    sum_list_of_string(calories.split('\n'))
    for calories
    in problem_text_split
]

print(max(per_elf))

# Part 2

sum(sorted(per_elf, reverse=True)[0:3])