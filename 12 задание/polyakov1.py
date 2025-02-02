
answer = 0
for n in range(0,1000):
    s = '>' + '0'*40 + '1'*n + '2'*40
    summa = [int(s[i]) for i in range(1,len(s))]
    
    if (len(str(sum(summa))) == 3) and (str(sum(summa))[0] == str(sum(summa))[1] == str(sum(summa))[2]):
        answer = n
        break
print(answer)

