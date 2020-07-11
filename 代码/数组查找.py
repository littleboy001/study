# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def find(self, target, array):
        # write code here
        print("-"*20)
        if target < array[0][0] or target > array[len(array)-1][len(array[0])-1]:
            print("targrt not found")
            return
        num = 0
        while target >= array[num][0]:
            if target > array[num][len(array[0])-1]:
                num += 1
            else:
                break
        if target in array[num]:
            print("target found")
        else:
            print("targrt not found")


target = eval(input("target:"))
array = list(eval(input("array:")))
print(target)
print(array)
s = Solution()
s.find(target,array)
