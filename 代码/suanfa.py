#！/usr/bin/env python
# -*- coding: utf8 -*-


def quick_sort(l:list,start: int,end: int):
    """快速排序"""
    if start > end:
        return
    i = start
    j = end
    flag = l[start]
    while True:
        while j > i and l[j] >= flag:
            j -= 1
        while i < j and l[i] <= flag:
            i += 1
        if i < j:
            l[i],l[j] = l[j],l[i]
        else:
            l[start],l[i] = l[i],l[start]#此处l[start]不能用flag替代，因为是用来交换列表值的
            break
    quick_sort(l,start,i-1)
    quick_sort(l,i+1,end)

def bubble_sort(l: list):
    """冒泡排序111"""
    for j in range(len(l)-1,0,-1):
        for i in range(0,j):
            if l[i] >= l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]

def choice_sort(l: list):
    """选择排序"""
    for j in range(len(l)-1):
        min_index = j
        for i in range(j+1,len(l)):
            if l[min_index] > l[i]:
                min_num = i
        l[min_index],l[j] = l[j],l[min_index]


if __name__ == "__main__":
    l = [13,12,6,2,3,2,5,4,6,8,7,9,11,10]
    print(f"l:{l}")
    #print([i for i in range(10,0,-1)])
    quick_sort(l,0,len(l)-1)
    print(f"quick_sort:{l}")
    bubble_sort(l)
    print(f"bubble_sort:{l}")
    choice_sort(l)
    print(f"choice_sort:{l}")
