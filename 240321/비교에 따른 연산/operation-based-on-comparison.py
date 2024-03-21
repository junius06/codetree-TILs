num = input()
arr = num.split()
a = int(arr[0])
b = int(arr[1])

if a > b:
    print(a * b)
else:
    print(b // a)