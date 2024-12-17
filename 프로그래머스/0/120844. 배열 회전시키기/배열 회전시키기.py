from collections import deque
def solution(numbers, direction):
    deque_numbers = deque(numbers)
    if direction == "right":
        deque_numbers.rotate(1)
    elif direction == "left":
        deque_numbers.rotate(-1)
    return list(deque_numbers)