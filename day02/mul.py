"""
求20以内奇数之积
"""
def mul_result():
    res = 1
    for i in range(1,21):
        if i % 2 == 1:
            res *= i
    return res 

print(mul_result())
