# utils.py
import random
from fractions import Fraction

def generate_operand(r: int):
    """随机生成自然数或真分数"""
    choice = random.random()
    if choice < 0.3:  # 30% 概率生成真分数
        numerator = random.randint(1, r - 1)
        denominator = random.randint(2, r)
        return f"{numerator}/{denominator}"
    else:
        return str(random.randint(0, r - 1))

def format_fraction(frac: Fraction):
    """将 Fraction 转换为输出格式"""
    if frac.denominator == 1:
        return str(frac.numerator)
    elif frac.numerator > frac.denominator:
        whole = frac.numerator // frac.denominator
        remainder = frac.numerator % frac.denominator
        if remainder == 0:
            return str(whole)
        return f"{whole}'{remainder}/{frac.denominator}"
    else:
        return f"{frac.numerator}/{frac.denominator}"

def is_duplicate(expr, existing_exprs):
    """判断表达式是否与已有的重复（仅简单判断加法/乘法交换律）"""
    simple = expr.replace(" ", "")
    for e in existing_exprs:
        if sorted(simple.replace("×", "*").replace("÷", "/")) == \
           sorted(e.replace(" ", "").replace("×", "*").replace("÷", "/")):
            return True
    return False
