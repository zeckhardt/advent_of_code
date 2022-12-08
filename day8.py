#COMPLETE
def check_up(x, y , trees, deep):
    up = x - deep
    if trees[up][y] < trees[x][y]:
        if up == 0:
            return True
        else:
            return check_up(x, y, trees, deep + 1)
    else:
        return False

def check_down(x, y , trees, deep):
    down = x + deep
    if trees[down][y] < trees[x][y]:
        if down == 4:
            return True
        else:
            return check_down(x, y, trees, deep + 1)
    else:
        return False

def check_left(x, y , trees, deep):
    left = y - deep
    if trees[x][left] < trees[x][y]:
        if left == 0:
            return True
        else:
            return check_left(x, y, trees, deep + 1)
    else:
        return False

def check_right(x, y , trees, deep):
    right = y + deep
    if trees[x][right] < trees[x][y]:
        if right == 4:
            return True
        else:
            return check_right(x, y, trees, deep + 1)
    else:
        return False


def solution(trees):
    visible_count = 16
    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees) - 1):
            if check_up(x, y, trees, 1) or check_down(x, y, trees, 1) or check_left(x, y, trees, 1) or check_right(x, y, trees, 1):
                visible_count += 1
    return visible_count


input = [[3, 0, 3, 7, 3],
         [2, 5, 5, 1, 2],
         [6, 5, 3, 3, 2],
         [3, 3, 5, 4, 9],
         [3, 5, 3, 9, 0]]

print(solution(input))
