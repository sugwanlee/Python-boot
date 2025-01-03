def solution(n):
    fac = 1                     # 팩토리얼 값을 담을 변수 선언
    for i in range(1,n+1):      # 1~n까지 돌리는 for문 생성
        fac = fac*i             # 팩토리얼(i!) 
        if fac == n:            # i! 값이 n과 같으면
            return i            # i를 반환
        elif fac >n:            # i! 값이 n보다 크면
            return i-1          # 바로 이전 i값(i-1)을 반환