# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if target < array[0][0] or target > array[len(array)-1][len(array[0])-1]:
            print("targrt not found")
            return
        num = 0
        while target >= array[num]:
            if target > array[len(array[0])-1]:
                num += 1
        if target in array[num]:
            print("target found")
        else:
            print("targrt not found")


target = eval(input("target:"))
array = list(eval(input("array:")))
s = Solution()
s.find(target,array)