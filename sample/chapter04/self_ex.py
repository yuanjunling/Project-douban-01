aList = [0,1,2,3,4,5,6,7,8,9]
print("aList[::] = ",aList[::])
print("aList[::-1] = ",aList[::-1])
print("aList[::2] = ",aList[::2])
print("aList[1::2] = ",aList[1::2])
aList[len(aList):]=[10]#列表尾部增加元素
print("aList[len(aList):]=[10] = ",aList)
aList[:0] = [-1,-2]#列表头部插入元素
print(aList)

import bisect

inter_list = []
bisect.insort(inter_list,8)
bisect.insort(inter_list,6)
bisect.insort(inter_list,5)
bisect.insort(inter_list,3)
bisect.insort(inter_list,7)
print(bisect.bisect_left(inter_list,6))
print(inter_list)

odd_list = [i for i in range(21) if i % 2==1] #列表生成式
print("odd_list = ",odd_list)

def head_itme(item):
    return item*item
odd_list1 = (head_itme(i) for i in range(21) if i % 2==1) #生成器表达式
print("odd_list1 = ",odd_list1)
for item in odd_list1:
    print(item)