import random
def getExpression():   #生成随机三位数内算法
    exp = ""
    symbol = random.choice(['+', '-', '*', '/'])  #生成随机符号
    if symbol == '+':
        n1 = random.randint(0, 99)
        n2 = random.randint(0, 99)
        result = n1 + n2
        exp = str(n1) + '+' + str(n2) + '='
    elif symbol == '-':
        n1 = random.randint(0, 99)
        n2 = random.randint(0, 99)
        n1,n2 = max(n1,n1),min(n1,n2)   #防止出现负数
        result = n1 - n2
        exp = str(n1) + '-' + str(n2) + '='
    elif symbol == '*':
        n1 = random.randint(0, 99)
        n2 = random.randint(0, 99)
        result = n1 * n2
        exp = str(n1) + '×' + str(n2) + '='
    else:
        n1 = random.randint(0, 99)
        n2 = random.randint(1, 99)
        result = n1 / n2
        exp = str(n1) + '÷' + str(n2) + '='
    print(exp)
    ans = input("请输入答案：")
    if int(ans) == result:
        print("回答正确")
    else:
        print("回答错误")
print("开始答题")
for i in range(10):
    getExpression()
print("作答完毕")
