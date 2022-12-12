import pathlib

path = pathlib.Path.cwd() / 'data' / 'day_6'
problem_text = path.read_text()


# Part 1

def find_distinct_chars_of_length_n(string: str, length_n: int):
    for idx, char in enumerate(string):
        string_subset = string[idx: idx + length_n]
        if len(string_subset) == len(set(string_subset)):
            return idx + length_n


print(find_distinct_chars_of_length_n(string=problem_text, length_n=4))

# Part 2
print(find_distinct_chars_of_length_n(string=problem_text, length_n=14))
