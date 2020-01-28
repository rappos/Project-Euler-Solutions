def collatz(numb):
    leng = 1
    while numb != 1:
        if numb % 2 == 0:
            numb = numb/2
            leng += 1
        else:
            numb = (3 * numb) + 1
            leng += 1

    return leng

max = 1
indx = 1
for i in range(1,1000001):
    temp = collatz(i)
    if temp > max:
        max = temp
        indx = i

print("indx: ",indx)
print("max: ",max)
