def solution(dots):
    dots.sort()
    width = abs(dots[0][0] - dots[3][0])
    length = abs(dots[0][1] - dots[3][1])
    print(dots)
    return width * length