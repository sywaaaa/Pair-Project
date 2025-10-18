# main.py
import argparse
from generator import generate_exercises
from checker import check_answers

def main():
    parser = argparse.ArgumentParser(description="小学四则运算题目自动生成与判分程序")
    parser.add_argument("-n", type=int, help="生成题目的数量")
    parser.add_argument("-r", type=int, help="生成题目中数值范围（必须指定）")
    parser.add_argument("-e", type=str, help="题目文件（用于判分）")
    parser.add_argument("-a", type=str, help="答案文件（用于判分）")

    args = parser.parse_args()

    # --- 模式判断 ---
    if args.e and args.a:
        print("🧮 正在进行判分...")
        check_answers(args.e, args.a)

    elif args.r is not None:
        # 生成模式
        n = args.n if args.n else 10
        print(f"🧩 正在生成 {n} 道题目（范围 < {args.r}）...")
        generate_exercises(n, args.r)
        print("✅ 已生成 Exercises.txt 与 Answers.txt 文件")

    else:
        # 参数不足
        print("❌ 参数错误！请使用以下命令格式：\n")
        print("生成题目：python main.py -n 10 -r 10")
        print("判分题目：python main.py -e Exercises.txt -a MyAnswers.txt")


if __name__ == "__main__":
    main()
