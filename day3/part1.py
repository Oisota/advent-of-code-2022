def main():
    """Solve the problem"""
    sum_priorities = 0

    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26
    all_letters = letters + letters.upper()
    assert len(all_letters) == 52

    priorities = { l: i + 1 for i, l in enumerate(all_letters)}


    with open('part1input.txt') as f:
        for line in f:
            n = len(line)
            mid = n // 2
            first = set(line[0:mid])
            second = set(line[mid:])
            common = first & second # set intersection
            first_common = next(iter(common))

            sum_priorities += priorities[first_common]

    print(sum_priorities)

if __name__ == '__main__':
    main()
