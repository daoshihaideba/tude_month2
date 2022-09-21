"""
1. 使用dict.txt单词本完成
   编写一行函数，参数传入一个单词，函数执行后返回这个单词
   对应的哪一行内容

   单词本特点： 每个单词占一行
              单词与解释之间有若干空格
              单词按照从小到达排列
"""
def query_word(word):
    fr = open("../day16/dict.txt", 'r')
    n = len(word) # 单词长度
    # 迭代每次取一行
    for line in fr:
        if line[:n] == word and line[n] == ' ':
            return line

res = query_word("much")
print(res)

# 解题方法2
def query_word(word):
    fr = open("../day16/dict.txt", 'r')
    # 迭代每次取一行
    for line in fr:
        tmp = line.split(' ') # 将一行内容按照空格切割
        if tmp[0] > word:
            break # 遍历到的单词已经大于word就肯定找不到了
        elif tmp[0] == word:
            return line

res = query_word("abc")
print(res)