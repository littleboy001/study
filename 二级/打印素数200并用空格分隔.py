ls = [1]
a = 2
while a <= 200:
    
    for i in range(2,a+1):
        if i<a and a % i == 0:
            ls.append(a)
            break
        elif i == a:
            break
        else:
            continue
    a += 1
#print(ls)
for i in ls:
    print(i,end = " ")      
        