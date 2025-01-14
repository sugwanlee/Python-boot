def solution(numbers, k):
    numbers_arr = numbers*(((k*2)+2)//len(numbers) + 1)
    return numbers_arr[2*(k-1)]