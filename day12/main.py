import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# old_name = ['memory', 'cpu', 'disk','寄存器']
# with open('day12/1.txt', 'r') as file:
#     data = file.read()
# print(data)
# print(old_name)
# a=[]
# i=0
# k=0
# while i<4:
#     a.append(0)
#     for old_name[i] in data:
#         a[i]+=1
#     i+=1
# for j in a:
#     print(j)
# print(np.identity(3, dtype=int))
a = np.array([1,2,3,4,5,6,7,8,9])
a.shape = (3,3)
pd.DataFrame(a).to_csv('day12/1.csv')
print(a[0])