n = int(input())
meetings = []
for i in range(n):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x : (x[1], x[0]))

end_time = 0
cnt = 0
for start, end in meetings:
    if start >= end_time:
        cnt += 1
        end_time = end
print(cnt)

    