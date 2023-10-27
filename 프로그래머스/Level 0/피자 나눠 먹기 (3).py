def solution(slice, n):
    return n // slice if n // slice == n / slice else n // slice + 1
