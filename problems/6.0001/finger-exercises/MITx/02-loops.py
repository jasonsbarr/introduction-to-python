# Exercise: while exercise 1

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# In this problem you'll be given a chance to practice writing some while
# loops.

# 1. Convert the following into code that uses a while loop.

# print 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
print("Goodbye!")

# Exercise: while exercise 2

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# 2. Convert the following into code that uses a while loop.

# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2
n = 10
print("Hello!")
while n > 0:
    if n % 2 == 0:
        print(n)
    n -= 1

# Exercise: while exercise 3

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we
# define end to be 6, your code should print out the result:

# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

end = 10
x = 0
sum = 0
while x <= end:
    sum += x
    x += 1
print(sum)

# Exercise: for exercise 1

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# In this problem you'll be given a chance to practice writing some for loops.

# 1. Convert the following code into code that uses a for loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints "Goodbye!"
for i in range(2, 11, 2):
    print(i)
print("Goodbye!")

# Exercise: for exercise 2

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# 2. Convert the following code into code that uses a for loop.

# prints "Hello!"
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2
print("Hello!")
for n in range(10, 1, -2):
    print(n)

# Exercise: for exercise 3

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# 3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we
# define end to be 6, your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

sum = 0
end = 10
for i in range(end + 1):
    sum += i
print(sum)
