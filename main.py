import decimal

# precision
decimal.getcontext().prec = 100

def PI(iterations):
    digit = 1
    for i in range(3,(iterations)*2,4):
        digit -= decimal.Decimal(1) / decimal.Decimal(i)
        digit += decimal.Decimal(1) / decimal.Decimal((i + 2))

    return 4 * digit 

if __name__ == "__main__":
    iterations = 1000000
    digit = PI(iterations)
    print(digit)
