def bank(money, years):
    summa = money
    percent = 10
    year = 1
    while year <= years:
        summa = summa + summa / percent
        year += 1
    return summa
