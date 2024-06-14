def f(money,interest,month)
    result = 0
    for i in range(12):
        result+=money*((interest+100)/100)**(month-i)
    return result
print(f(1000000,1.74,3))
