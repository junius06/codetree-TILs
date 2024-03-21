body = input()
arr = body.split()
height = int(arr[0])
weight = int(arr[1])

bmi = weight*100*100 // (height**2)
print(bmi)

if bmi >= 25:
    print('Obesity')