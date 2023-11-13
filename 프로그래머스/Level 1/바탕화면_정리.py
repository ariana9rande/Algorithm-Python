def solution(wallpaper):
    answer = []
    top = -1
    left = 51
    bottom = 0
    right = 0

    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            if top == -1:
                top = i
            bottom = i
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if left > j:
                    left = j
                if right < j:
                    right = j

    bottom += 1
    right += 1

    answer.append(top)
    answer.append(left)
    answer.append(bottom)
    answer.append(right)

    return answer


wallpaper = ["..........",
             ".....#....",
             "......##..",
             "...##.....",
             "....#....."]
print(solution(wallpaper))