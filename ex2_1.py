import numpy as np
import matplotlib.pyplot as plt

x=((3,3),(4,3),(1,1))     # 1,2 正实例   3 负实例
omega=np.array([0.,0.])
b=0.
eta=1

def sign(i):      # y_i
    if(i<2):
        return 1
    else:
        return -1

def loss_function_i(x_i,omega,b,sign):
    loss_function_i=0.
    a=[0.]*len(omega)
    a+=np.array(x_i)*np.array(omega)
    for i in range(len(omega)):
        loss_function_i+=a[i]
    loss_function_i+=b
    return loss_function_i*sign

j=1
while j:
    for i in range(len(x)):
        if(loss_function_i(x[i],omega,b,sign(i))<=0):
            print('loss_function_i of','x_'+str(i+1),'=',loss_function_i(x[i],omega,b,i),end='   ')
            omega+=eta*sign(i)*np.array(x[i])
            b+=eta*sign(i)
            print('omega=',omega,'  b=',b)
            break
        else:
            if(i==len(x)-1):
                j=0
print(omega)
print(b)

# 画图
xx=np.arange(0,5,0.01)
for i in range(len(x)):
    if(i<2):
        plt.scatter(x[i][0],x[i][1],c='b')
    else:
        plt.scatter(x[i][0],x[i][1],c='r')
if(omega[1]!=0):
    plt.plot(xx,-omega[0]*xx/omega[1]-b,c='black')
plt.show()