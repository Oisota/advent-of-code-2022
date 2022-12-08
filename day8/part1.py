def main():
    """Solve the problem"""
    
    # parse input into 2d list of lists of ints
    trees = []
    #input_file = './input-test.txt'
    input_file = './input.txt'
    with open(input_file) as f:
        for line in f:
            row = [int(s) for s in line.strip()]
            trees.append(row)

    # determine visibility
    perimeter_count = (len(trees[0])) + (len(trees) - 1) + (len(trees[0]) - 1) + (len(trees) - 2) # count perimeter trees as they're all visible
    visible_count = perimeter_count
    highest_score = 0
    # ranges are adjusted to not iterate edge trees
    for ri in range(1, len(trees) - 1): # ri is row index
        row = trees[ri]
        for ci in range(1, len(row) - 1): # ci is column index
            tree = row[ci]
            # need to check up/down/left/right of tree to see if its visible from edge

            # check visible from top
            visible_up = True
            up_score = 0
            for v in range(ri - 1, -1, -1): # iterate up rows, same column
                up_score += 1
                if tree <= trees[v][ci]:
                    visible_up = False
                    break
            # check visible from bottom
            visible_down = True
            down_score = 0
            for v in range(ri + 1, len(trees)):
                down_score += 1
                if tree <= trees[v][ci]:
                    visible_down = False
                    break
            # check visible left
            visible_left = True
            left_score = 0
            for v in range(ci - 1, -1, -1):
                left_score += 1
                if tree <= trees[ri][v]:
                    visible_left = False
                    break
            # check visible right
            visible_right = True
            right_score = 0
            for v in range(ci + 1, len(row)):
                right_score += 1
                if tree <= trees[ri][v]:
                    visible_right = False
                    break

            if visible_up or visible_down or visible_left or visible_right:
                visible_count += 1

            score = up_score * down_score * left_score * right_score
            if score > highest_score:
                highest_score = score

    print(f'Visible Count: {visible_count}')
    print(f'Highest Score: {highest_score}')


if __name__ == '__main__':
    main()