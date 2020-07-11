a = input("请输入一个小数：")
b = ""
for i in a:
    if i != ".":
        b += i
    else:
        break
print(eval(b))
