import sys

def main():
    """Solve the Problem"""

    elves = []
    current_index = 0

    # parse input
    with open('./day-1-input.txt') as f:
        total = 0
        for line in f:
            if line == '\n':
                elves.append(total)
                total = 0
            else:
                total += int(line)

    # find largest total (Part 1)
    print(sorted(elves)[len(elves) - 1])

    # find total of top 3 (Part 2)
    print(sum(sorted(elves)[len(elves) - 3:]))



if __name__ == '__main__':
    main()
