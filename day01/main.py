# -*- coding: utf-8 -*-
# 指定编码
import math
from enum import Enum
from email.policy import default
from cmath import sqrt
print(5*9/10.0)
# 强制类型转换
print((int)(5*9/10))
flag = True
# 需要缩进
if flag:
    print("be Careful")
# 循环，计算阶乘，交互式输入时需要加入空行以表示完成
i = 1
sum = 1
while i <= 100:
    sum = sum*i
    i += 1
print(sum)
# 数据输出到文件
# 读写a+，写w+，读r+,追加
fopen = open("test.txt", 'a+')
print('test', file=fopen)
fopen.close()
# 将上次表达式的值赋值给_
# round(_,2)
print('spam eggs')
print('doesn\'t')
# 以下会报错
# print('doesn't')
#
print("doesn't")
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
# \n会被看成换行符
print('C:\name\some')
# """将行尾添加到字符串中，\可以防止这种情况发生
print("""\
Display this usage message
""")
# 字符串连接
print("Hello!\n"*3+"Hi!")
# 此时会将两个字符串连接在一起
print('Py' 'thon')
str = "hello,"
# 不适用于变量
# print(str 'Python')
# 变量与字符串连接
print(str+'Python')
# 字符串索引，打印单个字符
print(str[5])
# 负数索引
print(str[-2])
# 字符串切片,不包括尾部字符，包括头部字符
print(str[0:2])
# 始终包括开头或结尾
print(str[:2]+str[2:])
# 注意索引超出范围的情况
# 字符串不可更改，因此不可改变它们中间的字符
# str[0]='h'
# 打印字符串长度
print(len(str))
print(type(str))
list1 = [1, 2, 3]
list2 = [3, 2, 1]
list2.extend(list1)
print(list2)
# 枚举类练习


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = "blue"


color = 'red'
# color = Color(input("enter the color"))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("I see green!")
    case Color.BLUE:
        print("I see blue!")
    case _:
        print("I see nothing!")
# 元组练习
test = (1, 2, 3, 4, 5, 6)
print(test.index(6))
# 字典练习
dict = {
    '001': '张三',
    '002': '李四',
    '003': '王五'
}
print(dict, len(dict))
print(dict['003'])
del dict['001']
print(dict)
dict['张三'] = '003'
print(dict)
if '003' in dict:
    print(dict['003'])
a = {'A', 'B', 'C'}
b = {'D', 'E', 'F'}
print(a.difference(b))
print(a-b)
# 函数练习


def fib():
    for i in range(2, 100):
        flag = 0
        for j in range(2, int(math.sqrt(i))):
            if not (i % j):
                flag = 1
                break
        if flag == 0:
            print(i, "是素数")


fib()
a = 3
print(a == 3 and 4)
