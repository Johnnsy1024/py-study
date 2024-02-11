import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "integers",  # 参数名
        metavar="N",
        type=int,  # 参数类型
        nargs="*",  # +:至少传入一个参数 *:0个或多个 N:必须传入N个参数 ?:0个或1个参数
        help="an integer for the accumulator",  # -h提供信息
    )
    parser.add_argument("--hello", default="hello world", help="Say hello to the world")
    parser.add_argument(
        "--sum",
        action="store_const",  # 将const设定的值存储到dest设定的变量
        dest="accumulate",  # action中至的变量
        const=sum,  # 当用户使用了--sum选项时，accumulate变量的值将是Python的内置函数sum
        default=max,  # 当用户没有使用--sum选项时，accumulate变量的值将是Python的内置函数max
        help="sum the integers (default: find the max)",
    )

    args = parser.parse_args()
    print(args.accumulate(args.integers))
