# -*- coding:utf-8 -*-

"""
Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]

目的：实现上面的功能
实现的方式：它实现的很巧妙，利用了递归。
    - 第一次运行这个函数的时候，创建了一个空的列表;
    - 然后依次递归原来的列表里面的元素，
        - 如果列表里面的是数，则append
        - 如果不是，则再递归，总会是数的，然后a.append
"""

def list_flatten(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            a = list_flatten(i, a)
        else:
            a.append(i)
    return a

input = [2, 1, [3, [4, 5], 6], 7, [8]]
print list_flatten(input)

"""
下面还是一步一步运行这个程序，看一下它的流程是怎样的：

1------------

a = []

for(第一次):
    a = [2]

for(第二次):
    a = [2, 1]

for(第三次):
    a = list_flatten([3, [4, 5], 6], a = [2,1])
        a = [2, 1]
        for(第一次)：
            a = [2, 1, 3]
        for(第二次)
            a = list_flatten([2, 1], a = [2, 1, 3])
                a = [2, 1, 3]
                for(第一次):
                    a = [2, 1, 3, 2]
                for(第二次)：
                    a = [2, 1, 3, 2, 1]
        for(第三次)
            a = [2, 1, 3, 2, 1, 6]

for(第四次)：
    a = [2, 1, 3, 2, 1, 6, 7]

for(第五次)：
    a = list_flatten([8], a = [2, 1, 3, 2, 1, 6, 7])
    for(第一次)：
        a = [2, 1, 3, 2, 1, 6, 7, 8]

结束，返回a


宏观的思路是：
1：
 a = list_flatten(i, a) 这句相当重要。
 (i, a)中a是已有的东西,就是我们前面已经得到的东西；i是我们新要添加的东西。
 它有两个选择：
    1. 如果里面有相应的数组或者元组，就选择第一个;
    2. 如果直接是数据，则就直接添加。

2：
 还有一个关键点我认为比较重要：就是括号[]这个东西是怎么取消的？
 - 这是通过 for i in l: 这句话取消的，取出 l 列表里面的数值i。


在我看来，本质就是括号怎么取消的，暂时理解到这里。
"""
