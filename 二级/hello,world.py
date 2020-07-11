def isnum(a):
    try:
        if a == 1:
            print("请输入大于1的整数:")
        else:   
            for i in range(2,a+1):
                if i<a and a % i != 0:
                    continue
                elif i<a and a % i == 0:
                    return False
                else:    
                    return True
            
    except:
        print("请输入整数:")
    
print(isnum(5))
