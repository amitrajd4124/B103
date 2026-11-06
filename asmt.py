for i in range(1, 51):
    print(i)


for i in range(50, 0, -1):
    print(i)


for i in range(1, 101):
    if i % 2 == 0:
        print(i)


for i in range(1, 101):
    if i % 2 != 0:
        print(i)


for i in range(1, 101):
    if i % 5 == 0:
        print(i)


sum = 0
for i in range(1, 51):
    sum = sum + i

print("Sum =", sum)


sum = 0
for i in range(1, 21):
    if i % 2 == 0:
        sum = sum + i

print("Sum =", sum)


sum = 0
for i in range(1, 21):
    if i % 2 != 0:
        sum = sum + i

print("Sum =", sum)


for i in range(1, 21):
    print(i)


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


n = int(input("Enter N: "))
count = 0

for i in range(1, n + 1):
    count = count + 1

print("Count =", count)


for i in range(1, 11):
    print(i * i)


for i in range(1, 11):
    print(i * i * i)


for i in range(100, 0, -5):
    print(i)


for i in range(1, 101):
    if i % 3 == 0 and i % 4 == 0:
        print(i)


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n * i)


n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i)


n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(i)
    if i == 20:
        break


for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()