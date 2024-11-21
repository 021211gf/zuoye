# a=int(input('请输入一个整数'))
# if a%2==0:
#     print(a,'是偶数')
# else:
#     print(a,'是奇数')
########################################################################
# a=int(input('请输入一个整数'))
# if a>=90and a<=100:
#     print(a,'A')
# else:
#     if a>=80 and a<90:
#         print(a,'B')
#     else:
#         if a>=70 and a<80:
#             print(a,'C ')
#         else:
#             if a>=60 and a<70:
#                 print(a,'D')
#             else:
#                 if a >= 0 and a < 60:
#                  print(a,'E')
#                 else:
#                         print('输入有误')
########################################################################
# answer=input('您是会员吗？y/n')
# money=float(input('请输入您的购物金额：'))
# if answer=='y':
#     if money>=200:
#         print('打八折，付款金额为：',money*0.8)
#     elif money>=100:
#         print('打九折，付款金额为：',money*0.9)
#     else:
#         print('不打折',money)
# else:
#     if money>=200:
#         print('打9.5折，付款金额为：',money*0.95)
#     else:
#         print('不打折',money)
#######################################
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第一个整数'))
# if num_a>=num_b:
#     print(str(num_a)+'大于等于'+str(num_b))
# else:
#     print(str(num_a)+'小于'+str(num_b))
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))

















