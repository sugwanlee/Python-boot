def solution(numbers):
    string = {"zero" : "0" , "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7",   "eight" : "8", "nine" : "9"}
    a = ""
    answer = ""
    for i in numbers:
        a += i
        if a in string:
            answer += string[a]
            a = ""
    return int(answer)