# COMPLETE
def solution(games):
    score = 0

    for game in games:
        if game[1] == 'X':
            if game[0] == 'A':
                score += (1 + 3)
            elif game[0] == 'B':
                score += (1 + 0)
            else:
                score += (1 + 6)
        elif game[1] == 'Y':
            if game[0] == 'A':
                score += (2 + 3)
            elif game[0] == 'B':
                score += (2 + 0)
            else:
                score += (2 + 6)
        else:
            if game[0] == 'A':
                score += (3 + 3)
            elif game[0] == 'B':
                score += (3 + 0)
            else:
                score += (3 + 6)

    return score


print(solution([['A', 'Y'], ['B', 'X'], ['C', 'Z']]))
