N = int(input())
count_full_time = 0
count_part_time = 0

for _ in range(N):
    line = input().split()
    participation_format = line[3] == 'True'
    if participation_format:
        count_full_time += 1
    else:
        count_part_time += 1

print(count_full_time, count_part_time)