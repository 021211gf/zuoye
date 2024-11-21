# import fp as fp
#
# print(520)
# print(3+1)
# print("helloworld")
#
# ###输出文件1.指定位置，输出文件使用file=fp
# fp=open('D:/test.txt','a+')#如果文件不存在就创建 存在就继续追加
# print('helloworld',file=fp)
# fp.close()
# print('hello','world','Python')
# ##输入函数input
# '''present=input('大圣想要什么礼物呢？')
# print(present,type(present))'''
# a=input('a=')
# b=input('b=')
# print(int(a)+int(b))
# a=int(input('a='))
# b=int(input('b='))
# print(a+b)
# #除以/ 整除//  取余%   幂运算**
# r=range(10)
# print(r)#range(0, 10)
# print(list(r))#range(0, 10)
# ########################
# r=range(1,10)
# print(r)#range(1, 10)
# print(list(r))#[1, 2, 3, 4, 5, 6, 7, 8, 9]
# ########################
# r=range(1,10,2)
# print(list(r))#[1, 3, 5, 7, 9]
# ###########################
# print(10 in r)#False,10不在r这个序列中
# print(9 in r)#True,9在r这个序列中
# print(9 not in r)#False，9在
# print(10 not in r)#True，10不在
# ###########range函数############
# a=range(1,20,1)
# print(list(a))#[1-19]
# print(range(1,101,1))#[1-100]
###########while循环#################
# a=int(input('请输入一个整数'))
# a=0
# sum=0
# while a<5:
#     sum+=a
#     a+=1
# print('sum='+str(sum))
###########while循环############
# a=1
# sum=0
# while a<101:
#     if not bool(a%2):#if a%2==0:  bool==0时为False
#         sum+=a
#     a+=1
# print('sum='+str(sum))
###########for in循环############
# for item in 'Python':#第一次去出来的值为p ，给p赋值为item，输出item
#     print(item)
# for i in range(10):
#     print(i)
# ##########如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
# for _ in range(1):
#     print('hello')
# ############for 循环求1到100之间的偶数和
# sum=0
# for b in range(1,101):
#     if b%2==0:
#         sum+=b
# print("1到100之间的偶数和",sum)
# ##################100到999之前的水仙花数
# for item in range(100,1000):
#     c=item%10#个位的数
#     d=item//10%10#十位的数 先整除在取余
#     e=item//100#百位的数
#     if c**3+d**3+e**3==item:#判断水仙花数  153=3**3+5**3+1**3
#         print(item)
################################
# for item in range(3):
#     pwd=input('请输入密码：')
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
#######################
# a=0
# while a<3:
#     pwd=input('请输入密码')
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         a+=1
#         print('密码不正确')
########################
# for item in range(1,51):
#     if item%5!=0:
#         continue
#     print(item)
########################9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+'*'+str(j),end='\t')#\t不换行输出
#     print()
########################
# lst=['hello','world','98','hello']
# print(lst[-3],lst[0])
# lst2=list(['hello','world','98'])
###############lst.index############
# lst=['hello','world','98','hello']
# print(lst.index('hello'))#如果列表中有相同元素会返回相同元素中的第一个元素
# lst=['hello','world','98']
# print(lst.index('hello',0,3))#指定范围2内查找
###################################[start:stop:step][开始:结束:步长]
lst=['10','20','30','40','50','60','70','80']
# print(lst[1:6:1])
# print('原列表',id(lst))
# let2=lst[1:6:1]
# print('切的片段',id(let2))
# print(lst[1:6])#默认步长为1
# print(lst[1:6:])#默认步长为1
# print(lst[1:6:2])
# print(lst[:6:2])#start采用默认
# print(lst[1::2])#stop采用默认
# #step为负数代表，第一个元素为列表的最后一个元素，最后一个元素为列表的第一个元素
# print(lst[::-1])#['80', '70', '60', '50', '40', '30', '20', '10']
# print(lst[6::-1])#['70', '60', '50', '40', '30', '20', '10']
#############################判断###################################
# lst=[10,20,'python','hello']
# print(10 in lst)#True
# print(1 in lst)#False
# print(1 not in lst)#True
# print('p' not in lst)#True
#############################################
#向列表末尾添加一个元素#########         添 加append
# lst=[10,20,30]
# print('添加元素之前',lst,id(lst))#[10, 20, 30]
# lst.append(100)
# print('添加元素之后',lst,id(lst))#[10, 20, 30, 100]
# lst2=['hello','world']
# # lst.append(lst2)
# # print('添加元素之后',lst,id(lst))#[10, 20, 30, 100, ['hello', 'world']]
# #向列表的末尾添加多个元素 extend
# # lst.extend(lst2)
# # print('添加元素之后',lst,id(lst))#[10, 20, 30, 100, 'hello', 'world']
# #在任意位置添加元素
# # lst.insert(2,90)
# # print('添加元素之后',lst,id(lst))#[10, 20, 90, 30, 100]
# lst3=[True,False,'hello']
# lst[1:]=lst3
# print('添加元素之后',lst,)#[10, True, False, 'hello']
# lst[1:1]=lst3
# print('添加元素之后',lst,)#[10, True, False, 'hello', 20, 30, 100]
################################################################
#######删除
# lst=[10,20,30,40,10,50,60]
# lst.remove(10)#从列表中移除一个元素，如果有重复元素只移除第一个元素
# print(lst)#[20, 30, 40, 10, 50, 60]
# # lst.remove(100)#移除列表中不存在的元素会报错
# #pop根据索引移除数据,移除指定位置元素,指定的索引不存在时会报错
# lst.pop(1)#如果不知道索引时会删除列表中的最后一个元素
# print(lst)#[20, 40, 10, 50, 60]
# new_list=lst[1:3]#产生新的列表
# print('原列表',lst)#[20, 40, 10, 50, 60]
# print('切片后的列表',new_list)#[40, 10]
# lst[1:3]=[]#不产生新的列表，就是创建一个空的列表
# print(lst)#[20, 50, 60]
# lst.clear()#   清除列表中所有元素
# print(lst)#[ ]
# #del语句会将整个列表对象删除
# del lst
# print(lst)
####修改
# lst=[10,20,30,40,10,50,60]
# lst[2]=100#一次修改一个值
# print(lst)#[10, 20, 100, 40, 10, 50, 60]
# lst[1:3]=[200,300,400]#改列表中的多个值
# print(lst)#[10, 200, 300, 400, 40, 10, 50, 60]
###################列表的排序方法###############
# lst=[20,40,10,50,15,70,60]
# print('排序之前的列表',lst)
# #开始排序，调用列表对象的sort方法，升序排序，排序在原列表上进行
# lst.sort()
# print('排序之后的列表',lst)#[10, 15, 20, 40, 50, 60, 70]
# #通过指定关键字参数，将列表中的元素进行降序排序
# lst.sort(reverse=True)#reverse=True升序     reverse=False降序
# print('排序之后的列表',lst)#[10, 15, 20, 40, 50, 60, 70]
#使用内置函数sorted（）对列表进行排序，会产生一个新的列表对象
# lst=[20,40,10,50,15,70,60]
# print('排序之前的列表',lst)
# new_list=sorted(lst)
# print('排序之后的列表',new_list)
# #通过指定关键字参数，将列表中的元素进行降序排序
# desc_list=sorted(lst,reverse=True)
# print('排序之后的列表',desc_list)
################列表成式
#[i表示列表元素的表达式   for  i为自定义变量 in range(1，10)为可迭代的对象]
# lst=[i for i in range(1,10)]
# print(lst)
# lst=[i*i for i in range(1,10)]
# print(lst)
# lst=[i for i in range(1,11,2)]
# print(lst)
################################
#字典
#第一种创建字典{}
# scores={'张三':100, '李四':98,'王五':45}
# print(scores)
# print(type(scores))
# #第二章创建dict（）
# student=dict(name='jack',age=20)
# print(student)
# #创建空字典
# d={}
# print(d)
################################################################‘
#获取字典中的值
# scores={'张三':100, '李四':98,'王五':45}
# #第一种方式使用[]
# print(scores['张三'])
# # print(scores['张四'])#KeyError: '张四'报错
# #第二种方式，使用get（）方法
# print(scores.get('张三'))
# print(scores.get('张四'))#None
# print(scores.get('麻七',99))#99  #99是在查找麻七所对应的value不存在时，提供的一个默认值
################################################################
# 字典的常用操作
# 键的判断
# scores={'张三':100, '李四':98,'王五':45}
# print('张三' in scores)#True存在
# print('张三' not in scores)#False不存在
# #删除
# del  scores['张三']#删除指定的key-value
# # scores.clear()#清空字典
# print(scores)
# #新增元素
# scores['陈六']=98
# print(scores)
# #修改元素
# scores['陈六']=100
# print(scores)
################################################################
# #获取所有的key
# scores={'张三':100, '李四':98,'王五':45}
# keys=scores.keys()
# print(keys)
# print(type(keys))
# print(list(keys))#将所有的key组成的视图转为列表
#
# #获取所有的value
# values=scores.values()
# print(values)
# print(type(values))
# print(list(values))#将所有的value组成的视图转为列表
#
# # 获取所有的key-value对
# items=scores.items()
# print(items)
# print(type(items))
# print(list(items))#将所有的key-value对组成的视图转为列表
# #转换后的列表元素是由元组组成

# # 字典的元素遍历
# scores={'张三':100, '李四':98,'王五':45}
# for item in scores:
#     print(item,scores[item],scores.get(item))
####字典的特点
# d={'name':'张三','name':'李四','name':'张三'}#key不允许重复
# print(d)
# d={'name':'张三','nikename':'张三'}#value可以重复
# print(d)
########字典生成式
#内置函数zip（）
# item=['Fruits','Books','Orther']
# prices=[96,78,85]
#
# d={item.upper():price    for   item ,price in zip(item,prices)}
# print(d)
################################
#元组        不可别序列，可别序列
# #可别序列
# lst=[10,20,30]
# print(id(lst))
# lst.append(45)
# print(id(lst))
# #不可别序列,不可增删改
# s='hello'
# print(id(s))
# s+='world'
# print(id(s))
##元组的创建方式
# #第一种使用（）
# t=('python','world',98)
# print(t)
# print(type(t))
#
# t2='python','world',98
# print(t2)
# print(type(t2))
# #####只有一个元素要加逗号“，”
# t3=('python',)#t3=('python')
# print(t3)#python
# print(type(t3))
# #内置函数
# t1=tuple(('Python','world',98))
# print(t1)
# print(type(t1))

#####空元组的创建方式
####空列表的创建方式
# lst=[]
# lst1=list()
# #空字典
# d={}
# d2=dict()
# #空元组
# t4=()
# t5=tuple()
#
# print('空列表',lst,lst1)
# print('空字典',d,d2)
# print('空元组',t4,t5)
################################
# t=(10,[20,30],40)
# print(t)
# print(type(t))
# print(t[0],type(t[0]),id(t[0]))
# print(t[1],type(t[1]),id(t[1]))
# print(t[2],type(t[2]),id(t[2]))
# ####尝试将t【1】修改为100
# print(id(100))
# #t[1]=100   #元组是不允许修改元素的
# #####由于【20,30】列表，而列表是可变序列，所以可以向列中添加元素，而列表的内存地址不变
# #元组中的对象如果可改变，就可以添加元素
# t[1].append(100)#向列表中添加元素
# print(t,id(t[1]))
################################
# t=('python','world',98)
# #第一种获取元组的方式，使用索引
# print(t[0])
# print(t[1])
# print(t[2])
# #第二种获取元组的方式，遍历元组
# for item in t:
#     print(item)
####集合的创建方式
# #第一种创建方式{}
# s={1,2,3,4,5,6,6}#集合中的元素不允许重复
# print(s)
# #使用内置函数set
# t=set(range(5))
# print(t,type(t))
# s2=set([1,2,3,3,4,5,5])
# print(s2,type(s2))
# s3=set([1,2,4,4,5,5,65])#集合中的元素是无序的
# print(s3,type(s3))
# s4=set('python')
# print(s4,type(s4))
# s5=set([1,2,3,4,4])
# print(s5,type(s5))
# #定义一个空集合
# s6={}
# print(type(s6))
#
# s7=set()
# print(s7,type(s7))
#集合的相关操作
#集合元素的判断操作
s={10,20,30,40,50}
print(10 in s)#True
print(100 in s)#False
print(10 not in s)#False
print(100 not in s)#True
#集合元素的新增操作
s.add(80)
print(s)
s.update({200,300,400})
print(s)
s.update([150,92])
print(s)
s.update((78,67,667))
print(s)
#集合元素的删除操作
s.remove(10)
print(s)
#删除指定元素
s.discard(400)#有会删除，没有不会报错
print(s)
s.pop()#删除一个元素
print(s)
s.clear()#清空
print(s)
