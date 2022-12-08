# COMPLETE
def solution(inp: str):
    pos = 0
    curr = ''

    while pos < len(inp) - 3:
        for l in range(pos, pos + 4):
            if inp[l] in curr:
                break
            else:
                curr += inp[l]

        if len(curr) == 4:
            return pos + 4
        else:
            pos += 1
            curr = ''




print(solution('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))
