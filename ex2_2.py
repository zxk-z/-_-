import numpy as np
import matplotlib.pyplot as plt

# 输入变量
X=((3,3),(4,3),(1,1)) 
l=len(X)
# 输出变量
Y=(1,1,-1)
# 学习率  (0,1]
eta=1
# Gram matrix
Gram=np.zeros((l,l))
for i in range(l):
    for j in range(l):
        Gram[i][j]=np.mat(X[i])*np.mat(X[j]).T
# 输出
alpha=[0.]*l
b=0.
# 误分条件, 直接用 已用 X定义好的Gram matrix
def mis_condition_i(X, Y, i, alpha, b):           
    a=0.
    for j in range(l):
        a+=alpha[j]*Y[j]*Gram[j][i]
    return Y[i]*(a+b)
# 主程序	
j=1
while j:
    for i in range(l):
        if(mis_condition_i(X,Y,i,alpha,b)<=0):
            alpha[i]+=1
            b+=Y[i]
            break
    else:
        if(i==l-1):
            j=0
# 最终结果
omega=np.array([0.,0.])
for i in range(l):
    omega+=alpha[i]*Y[i]*np.array(X[i])
print(omega)
print(b)
print(alpha)