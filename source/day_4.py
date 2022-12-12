import pathlib

# Part 1
path = pathlib.Path.cwd() / 'data' / 'day_4'
problem_text = path.read_text()

rows = problem_text.split('\n')

# part 1

# Test for function
row = rows[0]


def row_pair_to_range(row):
    range_pair = row.split(',')

    start_1, end_1 = tuple(map(int, range_pair[0].split('-')))
    start_2, end_2 = tuple(map(int, range_pair[1].split('-')))

    if start_1 >= start_2 and end_1 <= end_2 or start_1 <= start_2 and end_1 >= end_2:
        return 1
    else:
        return 0


range_pairs = [
    row_pair_to_range(row)
    for row
    in rows
]

sum(range_pairs)


# part 2

def get_overlap_flag(row):
    range_pair = row.split(',')

    start_1, end_1 = tuple(map(int, range_pair[0].split('-')))
    start_2, end_2 = tuple(map(int, range_pair[1].split('-')))

    if len(set(range(start_1, end_1 + 1)).intersection(set(range(start_2, end_2 + 1)))) >= 1:
        return 1
    else:
        return 0


range_pairs = [
    get_overlap_flag(row)
    for row
    in rows
]

sum(range_pairs)
