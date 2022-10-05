# 输出斐波那契数列
from ast import keyword


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(2000)
print(fib)
# 函数默认返回值为None
print(fib(0))
# 返回数列运算结果列表


def fib2(n):
    """Return a list."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# 打印列表
print(fib2(1000))
# 函数默认值参数


def ask_ok(prompt, retries=4, reminder='Try again'):
    while True:
        ok = 'yes'
        # ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 打印函数返回值
print(ask_ok('Do you want to quit?\n'))


def f(i):
    i = i+1
    print(i)


f(6)
# 默认值只计算一次
# 累积传递参数


def f(a, L=[]):
    L.append(a)
    return L


L = [4, 2, 3, 6, 5]

# 不共享默认值


def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# L为默认参数
# 累积传递参数
print(f(3))
print(f(2))
print(f(1))
# 不共享默认值
print(f1(3))
print(f1(2))
print(f1(1))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print('This parrot wouldn\'t ', action, end='')
    print(" if you put", voltage, action, end="")
    print(" lovely plumage the", type)
    print("It's", state, "!")


# 默认为voltage
print(parrot(1000))
# voltage无默认值，不能为空
print(parrot(voltage='10000', action='Voooom'))
# 传递三个参数
print(parrot('a million', 'bereft of life', 'jump'))
# 参数传递无效
# print(parrot(voltage=5.0, 'dead'))
# 无法对同一参数多次赋值
# parrot('110', voltage=220)


def cheeseshop(kind, *arguments, **keyword):
    print("Do you have any ", kind, "?")
    print('I\'m sorry, we \'re all out of ', kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keyword:
        print(kw, ":", keyword[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 冒泡排序
# 不是传址，不可直接传列表，需要复制列表后操作，返回新列表

L = [2, 1, 3, 5, 6, 7]


def bubblesort(iterable):
    new_list = list(iterable)
    i = 0
    while i < len(new_list) - 1:
        j = 0
        while j < len(new_list) - 1 - i:
            if (new_list[j] > new_list[j+1]):
                temp = new_list[j]
                new_list[j] = new_list[j+1]
                new_list[j+1] = temp
            j += 1
        i += 1
    return new_list


print(bubblesort(L))


