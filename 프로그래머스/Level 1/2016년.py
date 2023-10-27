def solution(a, b):
    weekday = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0

    for i in range(a - 1, 0, -1):
        days += month_days[i - 1]
    days += b

    return weekday[days % 7]
