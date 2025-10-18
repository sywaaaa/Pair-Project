# evaluator.py
import re
from fractions import Fraction

def parse_operand(s: str):
    """将字符串形式的数字（含分数、带分数）转为 Fraction"""
    s = s.strip()
    if "'" in s:  # 带分数，如 2'3/4
        whole, frac = s.split("'")
        num, den = frac.split("/")
        return Fraction(int(whole) * int(den) + int(num), int(den))
    elif "/" in s:  # 真分数，如 3/5
        num, den = s.split("/")
        return Fraction(int(num), int(den))
    else:  # 自然数
        return Fraction(int(s), 1)

def safe_eval(expr: str):
    """仅允许合法的运算符"""
    expr = expr.replace("×", "*").replace("÷", "/")
    expr = re.sub(r"(\d+)'(\d+)/(\d+)", r"(\1+\2/\3)", expr)
    return expr

def evaluate_expression(expr: str):
    """计算表达式结果（Fraction类型），非法或负值返回 None"""
    expr = safe_eval(expr)
    try:
        value = eval(expr, {"__builtins__": None}, {"Fraction": Fraction})
        if value < 0:
            return None
        return value
    except Exception:
        return None
