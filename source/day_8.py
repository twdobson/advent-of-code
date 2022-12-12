import pathlib

path = pathlib.Path.cwd() / 'data' / 'day_8'
problem_text = path.read_text()

stack_lines = problem_text.split('\n')

# Part 1
rows = [list(map(int, row)) for row in stack_lines]
columns = list(zip(*rows))  # transpose list

counter = 0
border_trees = len(rows) * 2 + len(columns) * 2 - 4

for row_idx, row in enumerate(rows):
    for idx in range(1, len(row)):
        tree_height = row[idx]
        if idx not in [0, 98] and row_idx not in [0, 98] and (
                tree_height > max(row[0:idx])  # max from the left
                or tree_height > max(row[idx + 1:])  # max from the right
                or tree_height > max(columns[idx][0:row_idx])  # max from above
                or tree_height > max(columns[idx][row_idx + 1:])  # max from below
        ):
            counter += 1

print(counter + border_trees)

# Part 2
best_scenic_score = 0
for row_idx, row in enumerate(rows):
    for idx in range(1, len(row)):
        tree_height = row[idx]

        if row_idx not in [0, 98] and idx not in [0, 98]:
            left_dist = 1
            right_dist = 1
            up_dist = 1
            down_dist = 1
            for view in range(1, len(row)):

                left_view = row[max(idx - view, 0):idx]
                right_view = row[idx: min(idx + view, 99)]

                up_view = columns[row_idx][max(idx - view, 0):idx]
                down_view = columns[row_idx][idx + 1: min(idx + view + 1, 99)]

                if max(left_view) < tree_height:
                    left_dist = len(left_view)

                if max(right_view) < tree_height:
                    right_dist = len(right_view)

                if max(up_view) < tree_height:
                    up_dist = len(up_view)

                if max(down_view) < tree_height:
                    down_dist = len(down_view)

                scenic_score = right_dist * left_dist * up_dist * down_dist

                if scenic_score > best_scenic_score:
                    best_scenic_score = scenic_score

# 1835 too low
