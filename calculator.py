"""安全的交互式四则运算计算器，运行：python3 calculator.py。"""

import math


def read_input(prompt):
    value = input(prompt).strip()
    if value.lower() == "quit":
        raise EOFError
    return value


def read_number(prompt):
    while True:
        try:
            number = float(read_input(prompt))
            if not math.isfinite(number):
                raise ValueError
            return number
        except ValueError:
            print("输入无效，请输入有限数字，或输入 quit 退出。")


def main():
    print("安全的计算器：支持 + - × ÷（也支持 * /）。")
    print("在任意输入处输入 quit 即可退出。")
    try:
        while True:
            operator = read_input("\n运算符：")
            if operator not in ("+", "-", "×", "÷", "*", "/"):
                print("运算符无效，请输入 + - × ÷。")
                continue

            left = read_number("第一个数字：")
            right = read_number("第二个数字：")
            if operator in ("÷", "/") and right == 0:
                print("除数不能为 0，请重新计算。")
                continue

            if operator == "+":
                result = left + right
            elif operator == "-":
                result = left - right
            elif operator in ("×", "*"):
                result = left * right
            else:
                result = left / right

            if math.isfinite(result):
                print(f"结果：{result:g}")
            else:
                print("结果超出数值范围，请使用较小的数字。")
    except (EOFError, KeyboardInterrupt):
        print("\n计算器已退出，再见！")


if __name__ == "__main__":
    main()
