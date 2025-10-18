# generator.py
import random
from evaluator import evaluate_expression
from utils import generate_operand, format_fraction, is_duplicate

def generate_expression(r):
    """随机生成一个四则运算表达式（运算符不超过3个）"""
    op_count = random.randint(1, 3)
    expr = generate_operand(r)
    for _ in range(op_count):
        op = random.choice(["+", "-", "×", "÷"])
        expr += f" {op} {generate_operand(r)}"
    return expr

def generate_exercises(n, r):
    """生成 n 道题目，并写入 Exercises.txt 与 Answers.txt"""
    expressions = []
    answers = []

    while len(expressions) < n:
        expr = generate_expression(r)
        if any(op in expr for op in ["÷ 0", "/ 0"]):
            continue  # 防止除以零
        value = evaluate_expression(expr)
        if value is None or value < 0:
            continue
        if is_duplicate(expr, expressions):
            continue
        expressions.append(expr)
        answers.append(format_fraction(value))

    with open("Exercises.txt", "w", encoding="utf-8") as f:
        for e in expressions:
            f.write(e + " =\n")

    with open("Answers.txt", "w", encoding="utf-8") as f:
        for a in answers:
            f.write(a + "\n")

    print(f"✅ 成功生成 {n} 道题目，结果保存在 Exercises.txt 与 Answers.txt 中。")
