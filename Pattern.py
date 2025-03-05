"""
Write a code to print this pattern

2  

3 5  

7 11 13  

17 19 23 29  

31 37 41 43 47
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


counter = 1
for i in range(5):
    for j in range(i + 1):
        print(nth_prime(counter), end=" ")
        counter += 1
    print()
