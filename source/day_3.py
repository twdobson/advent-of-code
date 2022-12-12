import pathlib
import string

# Part 1
path = pathlib.Path.cwd() / 'data' / 'day_3'
problem_text = path.read_text()

rows = problem_text.split('\n')

# part 1

lower_and_upper_alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# method of getting letter to priority
# def _prio(item):
#     if "a" <= item <= "z":
#         return ord(item) - ord("a") + 1
#     if "A" <= item <= "Z":
#         return ord(item) - ord("A") + 27
#     raise RuntimeError(f"not ok: {item}")

priority = dict(zip(
    lower_and_upper_alphabet,
    range(1, len(lower_and_upper_alphabet) + 1, 1)
))

priority_of_letters = [
    priority[
        set(row[:len(row) // 2]).intersection(set(row[len(row) // 2:])).pop()
    ]
    for row
    in rows
]

sum(priority_of_letters)

# part 2

list(zip(*(map(str.strip, rows),) * 3))

# total_priority = 0
# for idx in range(len(rows) // 3):
#     multiple = 3 * idx
#
#     total_priority += priority[
#         set(rows[multiple]).intersection(set(rows[multiple + 1])).intersection(set(rows[multiple + 2])).pop()
#     ]

total_priority = 0
for idx in range(len(rows) // 3):
    first, second, third = rows[slice(idx * 3, idx * 3 + 3)]

    total_priority += priority[
        set(first).intersection(set(second)).intersection(set(third)).pop()
    ]
