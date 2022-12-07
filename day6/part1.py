def main():
    """Solve the problem"""

    #distinct_chars = 4 # part 1
    distinct_chars = 14 # part 2

    with open('./part1input.txt') as f:
        line = next(f)
        print(f'Total Characters {len(line)}')
        for i in range(distinct_chars-1, len(line)): # start at distinct_chars distance into array
            chars = [line[i-j] for j in range(distinct_chars-1, -1, -1)] # look back distinct_chars back
            s = set(chars)
            if len(s) == distinct_chars: # all characters are different, otherwise set len would be < 4
                break

        print(f'Processed {i+1} Characters')


if __name__ == '__main__':
    main()
