# -*- coding: utf-8 -*-
# 指定编码
print(5*9/10.0)
# 强制类型转换
print((int)(5*9/10))
flag=True
# 需要缩进
if flag:
    print("be Careful")
# 循环，计算阶乘，交互式输入时需要加入空行以表示完成
i=1
sum=1
while i <= 100:
    sum=sum*i
    i+=1
print(sum)
# 数据输出到文件
# 读写a+，写w+，读r+,追加
fopen=open("test.txt",'a+')
print('test',file=fopen)
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
str="hello,"
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