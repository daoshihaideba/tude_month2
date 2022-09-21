"""
正则表达式
"""
import re

# 普通字符匹配自身
# res = re.findall("ab","abcdeabcda")
# print(res)

# .匹配一个字符
# res = re.findall('张.丰',"张三丰,张四丰,张五丰")
# print(res)

# 匹配字符集中的任意一个字符
# res =  re.findall('[ a-z]',"How are you!")
# print(res)

# 表示 o 可以出现0次或多次
# res = re.findall('wo*',"wooooo~~w!")
# print(res)

# 大写开头单词
# res =  re.findall('[A-Z][a-z]*',"How are you Jame")
# print(res)

# 表示 o 可以出现>=1次
# res = re.findall('wo+',"wooooo~~w!")
# print(res)

# 表示 o 可以出现0次或1次
# res = re.findall('wo?',"wooooo~~w!")
# print(res)

# 匹配数字
# res = re.findall('-?[0-9]+',"18岁的小战士在 -20 度站岗 2小时 8-20")
# print(res)

# 匹配手机号
# res = re.findall('1[3-9][0-9]{9}',"Jame:13886495728")
# print(res)

# 匹配qq号
# res = re.findall('[1-9][0-9]{5,10}',"Jame:12596688")
# print(res)

# 匹配开头结尾位置
# res = re.findall('^Jame',"Jame,hi")
# print(res)
#
# res = re.findall('Jame$',"hi,Jame")
# print(res)
#
# res = re.findall('^Jame$',"Jame")
# print(res)

# 匹配端口号
# res = re.findall('\d{1,5}',"Mysql: 3306, http:80")
# print(res)
# res = re.findall('\D+',"Mysql: 3306, http:80")
# print(res)

# 匹配普通字符（数字字母下划线） 和非普通字符
# res = re.findall('\w+',"server_port = 8888")
# print(res)
# res = re.findall('\W+',"server_port = 8888")
# print(res)

# 匹配空白字符和非空白字符
# res = re.findall('\w+\s+\w+',"hello    world")
# print(res)
# res = re.findall('\S+',"hello    world")
# print(res)

# 匹配 $ 使用 \$
res = re.findall('\$\d+',"工资 $3500")
print(res)

# 带有子组的正则表达式使用 search    返回匹配对象
# res = re.search('(ab)+',"info: ababababab")
# print(res.group()) # 获取对应匹配内容
# print(res.span()) # 获取匹配到的内容所在位置


res = re.search('(\d{1,3}\.?){4}',"IP: 192.168.5.43")
print(res.group())