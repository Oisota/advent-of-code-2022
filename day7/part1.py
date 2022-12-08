from dataclasses import dataclass

@dataclass
class Dir:
    name: str
    files: list
    dirs: list
    parent: None

    @property
    def size(self):
        """Sum file size, traversing all sub dirs"""
        file_sum = sum(f.size for f in self.files)
        sub_dirs_sum = sum(d.size for d in self.dirs)
        return file_sum + sub_dirs_sum

    def __repr__(self):
        return self.tree()

    def tree(self, indent=0):
        """Return directory tree as a string representation"""
        spaces = '|  ' * indent
        result = f'{self.name}/\n'
        if self.parent is None:
            result = f'{self.name}\n'
        for f in self.files:
            result += f'{spaces}|- {repr(f)}\n'

        for d in self.dirs:
            result += f'{spaces}|- {d.tree(indent+1)}'

        return result


    def walk_dirs(self):
        """iterate all dirs"""
        if self.parent is not None: # don't count root dir
            yield self

        for d in self.dirs:
            for d in d.walk_dirs():
                yield d

@dataclass
class File:
    name: str
    size: int

    def __repr__(self):
        return f'{self.name} <{self.size}>'

def main():
    """Solve the problem"""
    root = Dir('/', [], [], None)
    current_dir = root

    with open('./part1input.txt') as f:
        lines = f
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break
            parts = line.split(' ')
            if parts[0] == '$':
                cmd = parts[1]
                if cmd == 'cd':
                    p = parts[2].strip()
                    if p == '..': # cd up one dir level
                        current_dir = current_dir.parent
                    elif p == '/': # cd to root dir
                        current_dir = root
                    else: # cd into new dir
                        new_dir = Dir(parts[2].strip(), [], [], current_dir)
                        current_dir.dirs.append(new_dir)
                        current_dir = new_dir
                elif cmd == 'ls':
                    continue
            elif parts[0] == 'dir':
                pass
                #current_dir.dirs.append(Dir(parts[1], [] [])) # create new sub dir
                # probably don't need this as we should only create a new dir if we cd into it
            elif parts[0].isnumeric():
                current_dir.files.append(File(parts[1].strip(), int(parts[0])))


    #print(root)

    # part 1
    sizes = [d.size for d in root.walk_dirs() if d.size <= 100000]
    print(sizes)
    print(sum(sizes))

    # part 2
    total_space = 70000000
    update_space = 30000000

    unused_space = total_space - root.size
    print(f'Unused: {unused_space}')

    candidate_removal = [d.size for d in root.walk_dirs() if unused_space + d.size >= update_space]
    candidate_removal.sort()
    print(candidate_removal)
    print(candidate_removal[0])



if __name__ == '__main__':
    main()
