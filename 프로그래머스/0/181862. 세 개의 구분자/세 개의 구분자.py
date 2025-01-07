def solution(myStr):
    answer = []
    string = ""
    for i in myStr:
        if i not in "abc":
            string += i
        elif string != "":
            answer.append(string)
            string = ""
    if string != "":
        answer.append(string)
    return answer or ["EMPTY"]