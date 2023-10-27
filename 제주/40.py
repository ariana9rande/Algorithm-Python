limit = int(input())
n = int(input())
weight = [int(input()) for _ in range(n)]

weight_sum = 0
count = 0
sorted_weight = sorted(weight)

for i in sorted_weight:
    weight_sum += i
    count += 1
    if weight_sum > limit:
        count -= 1
        break


print(count)
