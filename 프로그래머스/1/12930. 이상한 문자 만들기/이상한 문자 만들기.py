def solution(s):
    answer = []
    word = ""
    for i in s.split(" "):
        for j, k in enumerate(i):
            if j % 2 == 1:
                word += k.lower()
            else:
                word += k.upper()
        answer.append(word)
        word = ""
    return " ".join(answer)