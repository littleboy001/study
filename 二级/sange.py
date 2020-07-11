hobbies = ""
for i in range(3):
    s = input("请输入你的爱好（最多三个，按q或Q结束）：")
    if s.upper() == "Q":
        break
    hobbies += s +","
print("你的爱好为：",hobbies)
    
