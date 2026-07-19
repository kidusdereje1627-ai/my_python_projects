class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}  # name -> Directory or File
    
    def get_size(self):
        total = 0
        for child in self.children.values():
            if isinstance(child, Directory):
                total += child.get_size()
            else:
                total += child.size
        return total

def parse_input(input_string):
    root = Directory("/")
    current_dir = root
    all_directories = [root]
    
    lines = input_string.strip().split("\n")
    for line in lines:
        if not line:
            continue
        tokens = line.split()
        
        if tokens[0] == "$":
            # Command execution
            cmd = tokens[1]
            if cmd == "cd":
                target = tokens[2]
                if target == "/":
                    current_dir = root
                elif target == "..":
                    if current_dir.parent:
                        current_dir = current_dir.parent
                else:
                    if target not in current_dir.children:
                        new_dir = Directory(target, current_dir)
                        current_dir.children[target] = new_dir
                        all_directories.append(new_dir)
                    current_dir = current_dir.children[target]
            elif cmd == "ls":
                continue
        else:
            # Output from ls
            if tokens[0] == "dir":
                dir_name = tokens[1]
                if dir_name not in current_dir.children:
                    new_dir = Directory(dir_name, current_dir)
                    current_dir.children[dir_name] = new_dir
                    all_directories.append(new_dir)
            else:
                size = int(tokens[0])
                file_name = tokens[1]
                if file_name not in current_dir.children:
                    current_dir.children[file_name] = File(file_name, size)
                    
    return root, all_directories

# (Input Data)
sample_input = """
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
625985 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
80330 d.log
5626152 d.ext
7214296 k
"""

if __name__ == "__main__":
    root, all_directories = parse_input(sample_input)
    
    # part 1: sum of directories with size at most 100000
    part1_total = sum(d.get_size() for d in all_directories if d.get_size() <= 100000)
    print(f"part 1 answer: {part1_total}")