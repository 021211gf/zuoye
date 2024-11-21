
import numpy as np

####已知条件
x0=np.pi / 6;x1=np.pi /4;x2=np.pi /3;
y0=1 / 2;y1=1 / (2 ** (1 / 2));y2=(3 ** (1 / 2) / 2)

####输入x
a=float(input("请输入需要估算的sin函数的自变量:"))
x = float(a) * (np.pi / 180)


#####一次拉格朗日插值法
def lagrange_one(flag):
#####当n=1时
    if flag == 1:
        ##x0,x1，拉格朗日插值
        lagrange = (x - x1) / (x0 - x1) * y0 + (x - x0) / (x1 - x0) * y1
    elif flag == 2:
        ##x1,x2,拉格朗日插值
        lagrange = (x - x2) / (x1 - x2) * y1 + (x - x1) / (x2 - x1) * y2
    return lagrange

####二次拉格朗日插值法
def lagrange_two():
###等n=2时
    ###x0,x1,x2,两次拉格朗日插值
    lagrange = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2)) * y0 + ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2)) * y1+ ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1)) * y2
    return lagrange




result_1=lagrange_one(1)
result_2=lagrange_one(2)
result_3=lagrange_two()
print(f'利用x0,x1，1次拉格朗日插值推导出sin{a}°的值为{result_1:.6f}')

print(f'利用x1,x2，1次拉格朗日插值推导出sin{a}°的值为{result_2:.6f}')

print(f'利用x0,x1,x2的2次拉格朗日插值推导出sin{a}°的值为{result_3:.6f}')

##误差

def erro(flag):  # 误差接受范围存在问题
    #外推的实际误差
    if flag == 1:
          # x0,x1外推的实际误差
          #x0的R（x）
        errolift = ((x - x0) * (x - x1) / 2) * (-1 / 2)
          #x1的R（x）
        erroright =(((x - x0) * (x - x1)) / 2) * (-((3 ** (1 / 2)) / 2))
        erroresult = np.sin(x) - result_1
        if erroresult > erroright and erroresult < errolift:
            print(f"利用x0,x1推导出sin{a}°的值的误差在可接受范围内，且误差为:{erroresult:.6f}")
        else:
            print(f"利用x0,x1推导出sin{a}°的值的误差过大，请重新设计。误差为：{erroresult:.6f}")
    #内推的实际误差
    elif flag == 2:
          # x1,x2外推的实际误差
          # x1的R（x）
        errolift = (((x) - x1)) * ((x - x2) / 2) * (-1 / (2 ** (1 / 2)))
          # x2的R（x）
        erroright = ((x) - x1) * ((x - (x2)) / 2) * (-((3 ** (1 / 2)) / 2))
        erroresult = np.sin(x) - result_2
        if erroresult > errolift and erroresult < erroright:
            print(f"利用x1,x2推导出sin{a}°的值的误差在可接受范围内，且误差为:{erroresult:.6f}")
        else:
            print(f"利用x1,x2推导出sin{a}°的值的误差过大，请重新设计。误差为：{erroresult:.6f}")
    #二次插值的实际误差
    elif flag == 3:
        # x0，x1,x2,二次插值的实际误差
          # x2的R（x）
        erroright = ((x) - x0) * (((x) - x1)) * ((x) - x2) * (-(3 ** (1 / 2)) / 2) / (3 * 2 * 1)
          # x0的R（x）
        errolift = ((x) - x0) * (((x) - x1)) * ((x) - x2) * (-1 / 2) / (3 * 2 * 1)
        erroresult = np.sin(x) - result_3
        if erroresult > errolift and erroresult < erroright:
            print(f"利用x0,x1,x2,2次拉格朗日插值推导出sin{a}°的值的误差在可接受范围内，且误差为:{erroresult:.6f}")
        else:
            print(f"利用x0,x1,x2,2次拉格朗日插值推导出sin{a}°的值的误差过大，请重新设计。误差为：{erroresult:.6f}")


erro(1)
erro(2)
erro(3)







