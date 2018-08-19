import time
import argparse


def f1():
    N = int(input())
    [int(input()) for _ in range(N)]


def f2():
    import sys
    input = sys.stdin.readline

    N = int(input())
    [int(input()) for _ in range(N)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int)
    args = parser.parse_args()

    if args.x == 1:
        f = f1
    else:
        f = f2

    t = time.time()
    f()
    print(time.time() - t)


if __name__ == '__main__':
    main()
