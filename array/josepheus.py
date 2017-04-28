# -*- coding:utf-8 -*-


def josephus(int_list, skip):
    skip -= 1
    id_x = 0
    new_list = []

    while len(int_list):
        id_x = (id_x + skip) % len(int_list)
        new_list.append(int_list.pop(id_x))

    print "每隔3个数取出一个数字：", new_list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
josephus(a, 3)

"""
abb_smile:
1. 为什么在循环一圈之后，所得的值刚好是我们要删的那个值？这是偶然还是必然？求余的本质是什么？
这与循环队列有什么关系？

2. skip -= 1 ?
因为列表会删去一个元素的，这样等于原来的id_x指向原来所指数据的下一个元素。。这样只要加上一个 skip-1 就行了

3. 循环队列 ？
3.1 对于多圈的情况，只有最后一圈是有效的----和这个没有什么大的关系，但我写上吧，好好体会
3.2 一圈过后，多出的那个，其实就是真正的东西，过去的一圈被 % 掉了，可以拿9个数画个圈子。

"""


