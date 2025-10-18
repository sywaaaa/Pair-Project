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


def convert_to_fraction(expr: str):
    """
    将表达式中的所有数字替换为 Fraction 表达式
    例： '3 + 1/2' -> 'Fraction(3,1) + Fraction(1,2)'
    """

    def repl(match):
        token = match.group()
        if "'" in token:  # 带分数
            whole, frac = token.split("'")
            num, den = frac.split("/")
            total_num = int(whole) * int(den) + int(num)
            return f"Fraction({total_num},{den})"
        elif "/" in token:  # 真分数
            num, den = token.split("/")
            return f"Fraction({num},{den})"
        else:  # 自然数
            return f"Fraction({token},1)"

    expr = expr.replace("×", "*").replace("÷", "/")
    expr = re.sub(r"\d+'?\d*/?\d*", repl, expr)
    return expr


def evaluate_expression(expr: str):
    """计算表达式结果（返回 Fraction），非法或负值返回 None"""
    expr = convert_to_fraction(expr)
    try:
        value = eval(expr, {"__builtins__": None}, {"Fraction": Fraction})
        if value < 0:
            return None
        return value
    except Exception:
        return None
