def solution(myString, pat):
    l = len(pat)
    if myString[len(myString)-1] == pat:
          return myString
    for i in range(len(myString)):
        if myString[-l-i:-i] == pat:
            return myString[0:len(myString)-i]