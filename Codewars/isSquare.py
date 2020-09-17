import math

def is_square(n):
    if n < 0:
        return False
    return int(math.sqrt(n))**2 == n


print(is_square(25))  # return True
print(is_square(28))  # return False
