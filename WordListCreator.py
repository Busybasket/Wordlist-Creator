import random
txt = 0
values = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","0","1","2","3","4","5","6","7","8","9",]
txtValues = []
dosya = open("WordList.txt","a",encoding="utf-8")
for i in range(0,1000000):
    a = random.choice(values)
    b = random.choice(values)
    c = random.choice(values)
    d = random.choice(values)
    e = random.choice(values)
    f = random.choice(values)
    lastValue = a+b+c+d+e+f
    print(lastValue)
    txtValues.append(lastValue)
    i = i+1
setList = set()
setList.update(txtValues)   
for i in range(0,10000000):
    deger = txtValues[i]
    dosya.write(txtValues[i]+"+")
    input(ébitti)