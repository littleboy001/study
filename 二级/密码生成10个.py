import random
b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@"
ls = []
num = 1
c = ""
random.seed(0x1010)
while num<=10:
    for i in range(10):
      
        c += random.choice(b)
  
    if ls == []:
        ls.append(c)
        num += 1
       
    elif ls != []:      
        
        for code in ls:
            
            
            if c[0] == code[0]:
               
                continue
            
        else:
                
            ls.append(c)
            num += 1
            
    c=''
                
    
for i in ls:
    print(i)
