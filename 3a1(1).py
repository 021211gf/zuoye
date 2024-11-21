from sympy import*
import math

x = symbols('x')

y = exp(x)

#计算基函数与原函数的内积
p = [None, None, None, None]
p[0] = integrate(y,(x,-1,1))
p[0] = round(p[0],4)
p[1] = integrate(x*y,(x,-1,1))
p[1] = round(p[1],4)
y1 = (((3*((x)**2))-1)/2)*y
p[2] = integrate(y1,(x,-1,1))
p[2] = round(p[2],5)
y2 = (((5*((x)**3))-3*x)/2)*y
p[3] = integrate(y2,(x,-1,1))
p[3] = round(p[3],5)
print('基函数与原函数的内积p0-p3分别为')
for i in range(4):
    print(p[i])

#计算基函数的系数
a = [None, None, None, None]
for i in range(4):
    a[i] = ((2*i+1)/2) * p[i]
    a[i] = round(a[i],4)
print('基函数的系数a1-a4分别为')
for i in range(4):
    print(a[i])
        
#三次最佳平方逼近多项式
s = a[0]*1 + a[1]*x + a[2]*(((3*((x)**2))-1)/2) + a[3]*(((5*((x)**3))-3*x)/2)
print('三次最佳平方逼近s=',s)
#平方误差计算
pfwc0 = integrate(y**2,(x,-1,1))
pfwc0 = round(pfwc0, 6)

pfwclist = [None, None, None, None]
pfwc1 = 0.000000
for i in range(4):
    pfwclist[i] = (2/(2*i+1))*(a[i])**2
    pfwc1 = pfwc1 + pfwclist[i]
    pfwc1 = round(pfwc1, 6)

pfwc = round(pfwc0-pfwc1, 6)

print('平方误差=',pfwc)




