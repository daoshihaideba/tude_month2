"""
字节串使用
是否所有的字符串都能转换为字节串   是的
是否所有的字节串都能转换为字符串   不是

空字节串为 假
"""
# 字节串变量 （纯英文字符常亮直接加b）
byte01 = b"hello"
print(type(byte01))
print(byte01)

# 将字符串转换为字节串  （非纯英文字符 或者 字符串变量）
byte02 = "你好".encode()
print(type(byte02))
print(byte02)

# 字节串 转换为字符串
print(byte02.decode())
# print(b'\xe4\xb6\xb7\xc1\xa1\xbd'.decode())

# 字节串与字节串可以拼接
byte03 = "中国".encode()
print((byte02 + byte03).decode())
