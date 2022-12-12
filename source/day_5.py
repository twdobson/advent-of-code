import pathlib

# Part 1
path = pathlib.Path.cwd() / 'data' / 'day_5'
problem_text = path.read_text()

stack_lines = problem_text.split('\n')
moves_start = stack_lines.index("")

stack_lookup = {
    idx: []
    for idx
    in range(1, 10)
}

for line in stack_lines[:moves_start - 1]:
    for idx in range(len(line) // 4 + 1):
        col = line[slice(idx * 4, idx * 4 + 3)]
        print(col)
        if col.rstrip() != '':
            stack_lookup[idx + 1].insert(0, col.rstrip())
#
# [N]         [C]     [Z]
# [Q] [G]     [V]     [S]         [V]
# [L] [C]     [M]     [T]     [W] [L]
# [S] [H]     [L]     [C] [D] [H] [S]
# [C] [V] [F] [D]     [D] [B] [Q] [F]
# [Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
# [P] [P] [C] [W] [W] [F] [W] [J] [C]
# [T] [L] [D] [G] [P] [P] [V] [N] [R]
#  1   2   3   4   5   6   7   8   9

moves = stack_lines[moves_start + 1:]

# Tests
move = moves[0]

copy_stack_lookup = stack_lookup.copy()

for move in moves:
    _, creates, _, from_col, _, to_col = move.split(' ')
    creates, from_col, to_col = int(creates), int(from_col), int(to_col)

    creates_moved = reversed(stack_lookup[from_col][-creates:])
    stack_lookup[from_col] = stack_lookup[from_col][:-creates]
    stack_lookup[to_col].extend(creates_moved)

    creates_moved = copy_stack_lookup[from_col][-creates:]
    copy_stack_lookup[from_col] = copy_stack_lookup[from_col][:-creates]
    copy_stack_lookup[to_col].extend(creates_moved)
    # crates_moved = copy_stack_lookup[from_col][-creates:]
    # copy_stack_lookup[from_col] = copy_stack_lookup[from_col][:-creates]
    # copy_stack_lookup[to_col].extend(crates_moved)

top_crates = []
for key in stack_lookup:
    top_crates.append(stack_lookup[key].pop().replace('[', '').replace(']', ''))

print(''.join([create for create in top_crates]))  # SVFDLGLWV

top_crates_2 = []
for key in copy_stack_lookup:
    top_crates_2.append(copy_stack_lookup[key].pop().replace('[', '').replace(']', ''))

print(''.join([create for create in top_crates]))  # DCVTCVPCL
