def main():
    """Solve the problem"""
    sum_priorities = 0

    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26
    all_letters = letters + letters.upper()
    assert len(all_letters) == 52

    priorities = { l: i + 1 for i, l in enumerate(all_letters)}


    with open('part2input.txt') as f:
        group = []
        for idx, line in enumerate(f):
            group.append(set(line.strip()))

            if (idx + 1) % 3 == 0:
                common = group[0] & group[1] & group[2] # set intersection
                first_common = next(iter(common))
                sum_priorities += priorities[first_common]
                group.clear()



    print(sum_priorities)

if __name__ == '__main__':
    main()
