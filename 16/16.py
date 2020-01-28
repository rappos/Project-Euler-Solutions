bigSum = 2**1000
bigStr = str(bigSum)

summa = 0
for i in range(len(bigStr)):
    summa += int(bigStr[i])

print(summa)
