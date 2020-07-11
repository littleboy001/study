a = "123huf 980--78  901hihi  ___  71 hhwug901 ---qguyig1389 "
num_count = 0
alpha_count = 0
indient_count = a.count(" ")
for i in a:
    if "0"<= i <="9":
        num_count += 1
    elif "a"<= i <="z" or "A"<= i <="Z":
        alpha_count += 1
other = len(a)-num_count-alpha_count-indient_count
print("{},{},{},{}".format(num_count,alpha_count,indient_count,other))
