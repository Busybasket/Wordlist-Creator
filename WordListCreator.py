# word list türkçe
import random

values = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","0","1","2","3","4","5","6","7","8","9","%","$","@","'",";","?","*","-","_",".","."]
txtValues = []
setList = set()
dosya = open("WordList.txt","a",encoding="utf-8")

for i in range(1,3010936484):
    d = i%1000000
    if d == 0:
        a = len(txtValues)
        setList.update()
        for i in range(0,a):
            dosya.write(txtValues[i] + "\n")
        dosya.close
        dosya = open("WordList.txt","a",encoding="utf-8")
        txtValues.clear()
    else:
        a = random.choice(values)
        b = random.choice(values)
        c = random.choice(values)
        d = random.choice(values)
        e = random.choice(values)
        f = random.choice(values)
        lastValue = a+b+c+d+e+f
        txtValues.append(lastValue)
setList.update(txtValues)

