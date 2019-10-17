def digits_sum(n):
    if n == 0:
        return 0
    return n%10 + digits_sum(int(n/10))

sum = digits_sum(123456)
print(sum)