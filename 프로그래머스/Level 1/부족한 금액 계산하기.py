def solution(price, money, count):
    total_price = 0
    i = 1
    while i <= count:
        total_price += price * i
        i += 1

    if total_price > money:
        return total_price - money
    else:
        return 0
