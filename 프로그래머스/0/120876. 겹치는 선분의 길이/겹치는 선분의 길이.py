def solution(lines):
    answer = []
    count = 0
    flat_lines = [list(range(x[0], x[1]+1)) for x in lines]
    flat_lines[0] = [x + 0.5 for x in flat_lines[0]][:-1]
    flat_lines[1] = [x + 0.5 for x in flat_lines[1]][:-1]
    flat_lines[2] = [x + 0.5 for x in flat_lines[2]][:-1]
    for i in flat_lines:
        answer += i
    for j in set(answer):
        if answer.count(j) >= 2:
            count += 1
    return count