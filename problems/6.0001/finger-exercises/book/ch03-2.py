s = "1.23,2.4,3.123"

sum = 0
for n in s.split(","):
    sum += float(n)

print(sum)
