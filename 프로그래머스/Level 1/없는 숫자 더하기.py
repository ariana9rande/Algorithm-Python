def solution(numbers):
    answer = 0
    for i in range(10):
        answer += i
    
    for i in numbers:
        answer -= i
        
    return answer
