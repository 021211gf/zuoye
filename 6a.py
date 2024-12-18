# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:56:27 2024

@author: Administrator
"""

from sympy import symbols
from sympy.solvers import solve
from sympy import Eq

# 使用symbols函数定义符号变量
x1, x2, x3 = symbols('x1 x2 x3')

# 定义方程组
equations = [
    Eq(x1 + x2 + x3, 16),
    Eq(4 * x2 - x3, 5),
    Eq(2 * x1 - 2 * x2 + x3, 1)
]

# 求解方程组
solution = solve(equations, (x1, x2, x3))

print("x1 =", solution[x1])
print("x2 =", solution[x2])
print("x3 =", solution[x3])