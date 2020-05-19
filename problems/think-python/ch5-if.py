# Exercise 1
import time

current = time.time()
print(current)
days = int(current // (60 * 60 * 24))
rem = current % (60 * 60 * 24)
hours = int(rem // (60 * 60))
rem = rem % (60 * 60)
minutes = int(rem // 60)
seconds = int(rem % 60)

print(f"It is {hours}:{minutes}:{seconds}, {days} days since the epoch.")


# Exercise 2
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")  # this should never print
    else:
        print("No, that doesn't work")


check_fermat(2, 3, 4, 3)
check_fermat(4, 3, 3, 5)


def is_triangle(s1, s2, s3):
    if s1 + s2 < s3 or s1 + s3 < s2 or s2 + s3 < s1:
        print("No")
    else:
        print("Yes")


is_triangle(3, 4, 5)
is_triangle(3, 4, 8)


def get_lengths():
    s1 = int(input("Enter the length of side 1: "))
    s2 = int(input("Enter the length of side 2: "))
    s3 = int(input("Enter the length of side 3: "))
    is_triangle(s1, s2, s3)


get_lengths()
