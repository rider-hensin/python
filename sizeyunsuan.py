import random
import profile
from fractions import Fraction


def getExpression():   #生成随机三位数内算法
    exp = ""
    result = 0
    symbol = random.choice(['+', '-', '*', '/'])  #生成随机符号
    n1 = random.randint(0, 99)
    n2 = random.randint(0, 99)
    if symbol == '+':
        result = n1 + n2
        exp = str(n1) + '+' + str(n2) + '='
    elif symbol == '-':
        n1, n2 = max(n1, n1), min(n1, n2)   #防止出现负数
        result = n1 - n2
        exp = str(n1) + '-' + str(n2) + '='
    elif symbol == '*':
        result = n1 * n2
        exp = str(n1) + '×' + str(n2) + '='
    else:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 / n2
        exp = str(n1) + '÷' + str(n2) + '='
    print(exp)     #输出表达式
    return result

def getExpression_true():   #生成真分数算法
    symbol = random.choice(['+', '-', '*', '/'])
    n1 = random.randint(1, 99)
    n2 = random.randint(n1, 99)
    num1 = Fraction(n1, n2)
    n1 = random.randint(1, 99)
    n2 = random.randint(n1, 99)
    num2 = Fraction(n1, n2)
    result = 0
    exp = ""
    if symbol == '+':
        result = num1 + num2
        exp = str(n1) + '+' + str(n2) + '='
    elif symbol == '-':
        num1, num2 = max(n1, n2), min(n1, n2)
        result = num1 - num2
        exp = str(n1) + '-' + str(n2) + '='
    elif symbol == '*':
        result = num1 * num2
        exp = str(n1) + '*' + str(n2) + '='
    else:
        num1, num2 = max(n1, n2), min(n1, n2)
        result = num1 / num2
        exp = str(n1) + '÷' + str(n2) + '='
    print(exp)
    return result

def main():
    print("开始答题")
    print("Please enter 'stop' to quit")
    while True:
        choose = random.randint(0, 1)
        if choose == 0:
            result = getExpression()
            user_result = input()
            if user_result == 'stop':
                break
            user_result1 = Fraction(user_result)
            if user_result1 == result:
                print("Answer is right")
            else:
                print("Error, the true answer is ", result)
        else:
            result = getExpression_true()
            user_result = input()
            if user_result == 'stop':
                break
            user_result1 = Fraction(user_result)
            if user_result1 == result:
                print("Answer is right")
            else:
                print("Error, the true answer is ", result)
main()
profile.run("getExpression()")
profile.run("getExpression_true()")
profile.run("main()")