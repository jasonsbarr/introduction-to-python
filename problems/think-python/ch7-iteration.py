import math


# Exercise 1
def mysqrt(num, epsilon=0.00001):
    x = num / 2
    while True:
        y = (x + num/x) / 2
        if y == x or abs(y - x) < epsilon:
            return y
        x = y


print(mysqrt(25))


def test_sqrt():
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    print("-\t---------\t------------\t----")
    for i in range(1, 11):
        print(f"{i}\t{mysqrt(i)}\t{math.sqrt(i)}\t{abs(mysqrt(i) - math.sqrt(i))}")


test_sqrt()
