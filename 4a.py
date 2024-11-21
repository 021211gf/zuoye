from scipy.integrate import quad
import numpy as np
from fractions import Fraction

# 定义积分函数
def f1(x):
    return (x-1)*(x-2)*(x-3) / ((0-1)*(0-2)*(0-3))

def f2(x):
    return (x-0)*(x-2)*(x-3) / ((1-0)*(1-2)*(1-3))

def f3(x):
    return (x-0)*(x-1)*(x-3) / ((2-0)*(2-1)*(2-3))

def f4(x):
    return (x-0)*(x-1)*(x-2) / ((3-0)*(3-1)*(3-2))

# 定义数组A来存储积分结果
A = np.zeros(4)

# 计算积分
A[0], _ = quad(f1, 0, 3)
A[1], _ = quad(f2, 0, 3)
A[2], _ = quad(f3, 0, 3)
A[3], _ = quad(f4, 0, 3)

# 将浮点数结果转换为分数
A_fractions = [Fraction(a).limit_denominator() for a in A]

# 定义一个函数来打印结果
def xishu():
    print("系数为：")
    for i, af in enumerate(A_fractions):
        print(f"A[{i}] = {af}")

# 调用函数
xishu()
print(f'本题中的积分约等于{A_fractions[0]}*f(0)+{A_fractions[1]}*f(1)+{A_fractions[2]}*f(2)+{A_fractions[3]}*f(3)')