def isnum(a):
    if type(eval(a)) == type(1) or type(eval(a)) == type(1.1) or type(eval(a)) == type(1+1j):
        return True
    else:
        return False
    
print(isnum("135"))
