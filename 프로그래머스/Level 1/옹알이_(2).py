def solution(babbling):
    arr = ["aya", "ye", "ma", "woo"]
    answer = 0
    for item in babbling:
        for s in arr:
            if s in item and s * 2 not in item:
                print(f"before item = {item}")
                item = item.replace(s, " ")
                print(f"after item = {item}")

        if not item.replace(" ", ""):
            print("answer += 1")
            answer += 1
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))
