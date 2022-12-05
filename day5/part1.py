import pprint

def main():
    """Solve the problem"""

    stacks = []

    with open('./part1input.txt') as f:
        # determine how many stacks we have
        for line in f:
            if line.startswith(' 1'):
                parts = line.replace(' ', '').strip()
                for _ in parts:
                    stacks.append([])
                break

        l = len(stacks) * 4
        letter_positions = list(range(1, l, 4)) # line index positions of stack letters

    # parse input into stack data structure
    with open('./part1input.txt') as f:
        for line in f:
            if line.startswith('['):
                for idx, pos in enumerate(letter_positions):
                    letter = line[pos]
                    if letter.isalpha():
                        stack = stacks[idx]
                        stack.insert(0, letter)
            else:
                break

    pprint.pprint(stacks)

    with open('./part1input.txt') as f:
        for line in f:
            if line.startswith('move'):
                parts = line.split(' ')
                count = int(parts[1]) # num crates to move
                src = int(parts[3]) - 1 # source stack
                dst = int(parts[5]) - 1 # destination stack

                # part 1
                #for _ in range(count):
                #    letter = stacks[src].pop()
                #    stacks[dst].append(letter)

                # part 2
                temp_stack = []
                for _ in range(count):
                    letter = stacks[src].pop()
                    temp_stack.append(letter) # push onto temp stack

                for _ in range(count):
                    letter = temp_stack.pop()
                    stacks[dst].append(letter)

                

    for s in stacks:
        print(s[len(s) - 1])

if __name__ == '__main__':
    main()
