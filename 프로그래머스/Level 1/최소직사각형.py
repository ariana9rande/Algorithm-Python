def solution(sizes):
    max_value = 0
    for i in sizes:
        if i[1] > i[0]:
            i[0], i[1] = i[1], i[0]
    
    sizes.sort(key = lambda x: x[0], reverse = True)
        
    for i in sizes:
        if i[1] > max_value:
            max_value = i[1]
        
    return sizes[0][0] * max_value
