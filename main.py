# main.py
import argparse
from generator import generate_exercises
from checker import check_answers

def main():
    parser = argparse.ArgumentParser(description="四则运算题目生成与判定程序")

    parser.add_argument("-n", type=int, help="生成题目数量")
    parser.add_argument("-r", type=int, help="题目中数值范围（必须）")
    parser.add_argument("-e", type=str, help="题目文件路径")
    parser.add_argument("-a", type=str, help="答案文件路径")
    args = parser.parse_args()

    if args.e and args.a:
        check_answers(args.e, args.a)
    elif args.r is not None and args.n:
        generate_exercises(args.n, args.r)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
