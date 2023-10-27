student = input().split()
score = list(map(int, input().split()))

print(dict(zip(student, score)))
