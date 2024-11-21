#转义字符\n换行
print('hello\nworld')#\n换行
print('hello\tworld') #\t填充制表位
print('helloooo\tworld')
print('hello\rworld')#\r替代，world将hello覆盖
print('hello\bworld')#\b是退一个格
print('http:\\\\www.baidu,com')
print('老师说：\'大家好\'')#\ 输出中间的内容\
#不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')#输出hello\nworld
#最后一个字符不能是\一个\不行两个\可以
print(r'hello\nworld\\')
#import导入keyword关键字print输出         保留字
import keyword
print(keyword.kwlist)
#'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
# 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield'不允许使用
#id内存地址 type 类型str
name='玛利亚'           #输出
print('标识',id(name))#标识 2037627914064
print('类型',type(name))#类型 <class 'str'>
print('值',name)#值 玛利亚
#int整数类型 float浮点数类型   bool布尔类型  str字符串类型'xxx'
#默认十进制  二进制要  0b010101   八进制要  0o156   十六进制要  0x1EAF  7855
#bool ture表示1真 false表示0 假
a=1.0
print(str(a),type(str(a)))
print(int(a),type(int(a)))
