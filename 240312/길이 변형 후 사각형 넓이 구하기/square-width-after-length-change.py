num = input()
num = num.split()
w = int(num[0])
h = int(num[1])

w += 8
h *= 3

print(w)
print(h)
print(w * h)