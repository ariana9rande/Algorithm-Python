# dictionary 쓸 필요 x, 나이를 int로 캐스팅한 뒤에 key로 삼아서 정렬해야함
def solution(arr):
    sortedArr = sorted(arr, key=lambda x: int(x.split()[0]))
    return sortedArr


N = int(input())
arr = [input() for _ in range(N)]
for item in solution(arr):
    print(item)