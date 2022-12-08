# COMPLETE
def solution(cals):
    sums = []
    for elf in cals:
        sums.append(sum(elf))

    hi = max(sums)
    return sums.index(hi) + 1


print(solution([[1000, 2000, 3000], [4000], [5000], [7000, 8000, 9000], [10000]]))