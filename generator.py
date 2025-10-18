# generator.py
import random
from evaluator import evaluate_expression
from utils import generate_operand, format_fraction, is_duplicate

def generate_expression(r):
    """随机生成一个支持括号的四则运算表达式（运算符 ≤ 3）"""
    op_count = random.randint(1, 3)
    tokens = [generate_operand(r)]

    # 随机添加运算符与操作数
    for _ in range(op_count):
        op = random.choice(["+", "-", "×", "÷"])
        tokens.append(op)
        tokens.append(generate_operand(r))

    # 随机加入括号（概率 50%）
    expr = " ".join(tokens)
    if op_count >= 1 and random.random() < 0.5:
        expr = add_random_parentheses(tokens)

    return expr

def add_random_parentheses(tokens):
    """
    在表达式中随机加括号，保证语法合法
    例如 ['3', '+', '2', '×', '4'] -> '(3 + 2) × 4'
    """
    ops = [i for i, t in enumerate(tokens) if t in ["+", "-", "×", "÷"]]
    if not ops:
        return " ".join(tokens)

    # 随机选择一个操作符，给它的左右各加一层括号
    idx = random.choice(ops)
    left = max(0, idx - 1)
    right = min(len(tokens) - 1, idx + 1)

    new_tokens = tokens[:left] + ["("] + tokens[left:right+1] + [")"] + tokens[right+1:]
    return " ".join(new_tokens)

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
