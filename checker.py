# checker.py
from evaluator import evaluate_expression
from utils import format_fraction

def check_answers(exercise_file, answer_file):
    """比对答案文件与标准答案，输出 Grade.txt"""
    with open(exercise_file, "r", encoding="utf-8") as f:
        exercises = [line.strip(" =\n") for line in f if line.strip()]
    with open(answer_file, "r", encoding="utf-8") as f:
        answers = [line.strip() for line in f if line.strip()]

    correct, wrong = [], []
    for i, (expr, ans) in enumerate(zip(exercises, answers), start=1):
        val = evaluate_expression(expr)
        std = format_fraction(val) if val is not None else None
        if std == ans:
            correct.append(i)
        else:
            wrong.append(i)

    with open("Grade.txt", "w", encoding="utf-8") as f:
        f.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")

    print(f"✅ 判题完成，结果已保存至 Grade.txt")
