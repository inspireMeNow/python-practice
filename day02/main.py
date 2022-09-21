square=[1,4,9,16,25]
print(square)
# 列表索引访问
print(square[0]+square[1]+square[-1])
# 列表切片
print(square[0:3]+square[4:5])
# 列表连接
print(square[0:3]+[36,49,64,81,100])
# 返回列表副本
print(square[:])
# 计算三次方
print(4**3)
# 列表可变
square[3]=64
print(square[:])
# append()列表末尾添加新项目
square.append(216)
print(square)
# len()也适用于列表
print(len(square))
# 多重赋值，右侧表达式先被计算
a,b=0,1
c=0
print(a,b,c)
while a <= 100 :
    if(a==89):
        print( a) #有换行符
    else:
        print( a,end = ', ') #避免换行符
    # a, b = b, a+b
    c = b
    b = a + b
    a = c
print('The value is ',256*256)
x=0
# 输入数字，注意类型转换
# x=int(input("input a number:"))
if(x < 0):
    x=0
elif(x == 0):
    print('zero')
else:
    print('more')
words = ['windows', 'linux', 'macos']
for w in words:
    print(w,len(w))
users = {'Hans': 'active', 'Éléonore': 'inactive', 'duan': 'active'}
for user,status in users.copy().items(): # 复制到迭代器
    if status == 'inactive':
        del users[user] # 删除元素
print(users)
active_users = {}
for user, status in users.items(): # user,status分别代表key和value
    if status == 'active':
        active_users[user] = status # 添加元素
print(active_users)
# range()函数,生成算术级数
for i in range(5,10):
    print(i)
print(list(range(-10,-100,-30))) # -30表示增量，-10和-100表示范围
# sum()求和
print(sum(list(range(-10,-100,-30))))
# def定义函数
def initlog(*args):
    pass # 需要语句但程序不需要操作时使用，即对程序运行无影响
def http_error(status):
    match status:
        case 400|404|418:
            return "Bad request"
        case 417:
            return "Not found"
        case _:
            return "Something wrong"
print(http_error(404))
