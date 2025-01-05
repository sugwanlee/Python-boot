def solution(my_string):
    answer = 0                      # 답으로 제출할 변수 선언
    number = "0"                    # 연속된 수는 하나의 수로 간주하기 위한 number 변수
    for i in my_string:             # my_string에서 하나씩 꺼내오기
        if i.isdigit():       # i가 자연수인지 판별
            number += i             # number에 숫자인 문자 더해주기
        else:
            answer += int(number)   # 숫자 외의 값이 나오면 number에 들어있는 값 숫자로 바꿔서 answer에 더해주기
            number = "0"            # 더한 뒤 number 초기화
    answer += int(number)           # my_string의 마지막 index위치의 값이 숫자일 경우를 위한 코드
    return answer