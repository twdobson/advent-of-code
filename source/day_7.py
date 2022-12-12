import pathlib

path = pathlib.Path.cwd() / 'data' / 'day_7'
problem_text = path.read_text()

stack_lines = problem_text.split('\n')

file_structure_example = [
    {'/': ['fa', 'fb', 'fc']},
    {
        'f1': ['fa1', 'fa2', 'fa3'],
        'fb': ['fb1', 'fb2', 'fb3']
    }
]

file_structure_example[1]

file_structure = [{'/': []}]

a = {1: 'one'}
a.update({2: 'two'})

current_level = None
for line in stack_lines:

    action = line

    if action == '$ cd /':
        current_level = 0
    elif action == '$ cd ..':
        current_level -= 1
    elif '$ cd ' in action:  # this is the action 'cd <some folder>'
        folder = action.replace('$ cd ', '')
        action += 1
    elif action == '$ ls':
        pass

    else:  # no action, typically after a list
        if 'dir ' in action: # if folder, add to tree
            folder = action.replace('dir ', '')
            if folder not in file_structure[current_level].keys():
                file_structure[current_level].update({folder: []})
        else:

            ...

