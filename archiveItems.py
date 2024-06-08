import os

def writeItem(item):
    parent_dir = os.path.abspath(os.getcwd())
    target_dir = "archive"
    target_file = "output.txt"

    path = os.path.join(parent_dir, target_dir)

    if not os.path.isdir(path):
        os.mkdir(path)
    
    path = os.path.join(path, target_file)

    with open(path, 'a+') as f:
        f.write(f'{item}\n')
