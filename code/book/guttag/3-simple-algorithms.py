# # Find the cube root of a perfect cube
# x = int(input("Enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, "is not a perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print("Cube root of", x, "is", ans)

# Find the cube root of a perfect cube (for loop)
# x = int(input("Enter an integer: "))
# for ans in range(0, abs(x) + 1):
#     if ans**3 >= abs(x):
#         break
# if ans**3 != abs(x):
#     print(x, "is not a  perfect cube")
# else:
#     if x < 0:
#         ans = -ans
#     print("Cube root of", x, "is", ans)

# total = 0
# for c in "12345678":
#     total = total + int(c)
# print(total)

# x = 5000
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += step
#     numGuesses += 1
# print("numGuesses =", numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print("Failed on squre root of", x)
# else:
#     print(ans, "is close to the square root of", x)

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epsilon:
    print("low =", low, "high =", high, "ans =", ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("numGuesses =", numGuesses)
print(ans, "is close to square root of", x)
