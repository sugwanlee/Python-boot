def solution(array, height):
    array.sort(reverse=True)
    a = []
    for i in array:
        if i > height:
            a.append(i)
        elif i <= height:
            break
    return len(a)