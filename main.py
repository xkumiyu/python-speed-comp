import argparse
import os
import pathlib
import random
import timeit
from operator import itemgetter

import numpy as np
import pandas as pd


def stdin(n_repeat, n_number, i) -> list:
    tmp = pathlib.Path('tmp')
    for _ in range(n_repeat * n_number):
        os.system('python stdin.py {} < data/N100000.txt >> {}'.format(i, tmp))
    with tmp.open() as f:
        data = [
            sum([float(f.readline()) for _ in range(n_number)]) / n_number
            for _ in range(n_repeat)
        ]
    os.remove('tmp')
    return data


def sort1(A):
    A.sort()


def sort2(A):
    sorted(A)


def sort3(A):
    A.sort(key=lambda x: x[1])


def sort4(A):
    A.sort(key=itemgetter(1))


def sort5(A):
    sorted(A, key=lambda x: x[1])


def sort6(A):
    sorted(A, key=itemgetter(1))


def loop1(N):
    for _ in range(N):
        pass


def loop2(N):
    for i in range(N):
        i


def loop3(N):
    i = 0
    while i < N:
        i += 1


def loop4(A):
    for i in range(len(A)):
        A[i]


def loop5(A):
    for a in A:
        a


def list1(N):
    [None] * N


def list2(N):
    [None for _ in range(N)]


def list6(N):
    [[None] * N for _ in range(N)]


def list7(N):
    [[None for _ in range(N)] for _ in range(N)]


def list3(N):
    A = []
    for i in range(N):
        A.append(i)


def list4(N):
    A = [None] * N
    for i in range(N):
        A[i] = i


def list5(N):
    A = [i for i in range(N)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_repeat', type=int, default=10)
    parser.add_argument('--n_number', type=int, default=10)
    parser.add_argument('--out', default='record.csv')
    args = parser.parse_args()

    record = pd.DataFrame(columns=['time', 'exp', 'func', 'param1', 'param2'])

    def to_df(data: list, exp: str, func: str, param1=None,
              param2=None) -> pd.DataFrame:
        N = len(data)
        data = pd.DataFrame(
            np.array([data, [exp] * N, [func] * N, [param1] * N,
                      [param2] * N]).T,
            columns=record.columns)
        data['time'] = data['time'].astype('float32')
        return data

    def do(df,
           func,
           param,
           exp_name,
           func_name,
           param1_name=None,
           param2_name=None):
        res = timeit.repeat(
            lambda: func(param), repeat=args.n_repeat, number=args.n_number)
        data = [x / args.n_number for x in res]
        df = pd.concat(
            [df,
             to_df(data, exp_name, func_name, param1_name, param2_name)],
            ignore_index=True)
        return df

    # stdin
    for i, func_name in [(1, 'input()'), (2, 'sys.stdin.readline()')]:
        data = stdin(args.n_repeat, args.n_number, i)
        record = pd.concat(
            [record, to_df(data, 'stdin', func_name)], ignore_index=True)

    # sort
    N = 10**6
    X = [random.random() for _ in range(N)]
    Y = [random.random() for _ in range(N)]
    for max_A in [10**4, 10**6]:
        A = [int(x * max_A) for x in X]
        for func, func_name in [(sort1, 'sort()'), (sort2, 'sorted()')]:
            record = do(record, func, A, 'sort1', func_name, N, max_A)

        A = [[int(x * max_A), int(y * max_A)] for x, y in zip(X, Y)]
        for func, func_name in [(sort3, 'A.sort(key=lambda x: x[1])'),
                                (sort4, 'A.sort(key=itemgetter(1))'),
                                (sort5, 'sorted(A, key=lambda x: x[1])'),
                                (sort6, 'sorted(A, key=itemgetter(1))')]:
            record = do(record, func, A, 'sort2', func_name, N, max_A)

    # loop
    for N in [10**5, 10**6, 10**7]:
        loop_list = [(loop1, 'for _ in range(N)'),
                     (loop2, 'for i in range(N)'), (loop3, 'while i < N')]
        for func, func_name in loop_list:
            record = do(record, func, N, 'loop1', func_name, N)

        A = [0] * N
        loop_list = [(loop4, 'for i in range(len(A))'), (loop5, 'for a in A')]
        for func, func_name in loop_list:
            record = do(record, func, A, 'loop2', func_name, N)

    # list
    for N in [10**5, 10**6, 10**7]:
        list_func = [(list1, '[None] * N'), (list2,
                                             '[None for _ in range(N)]')]
        for func, func_name in list_func:
            record = do(record, func, N, 'list1', func_name, N)
        list_func = [(list3, 'append()'), (list4, 'A[i] = i'),
                     (list5, 'A = [i for i in range(N)]')]
        for func, func_name in list_func:
            record = do(record, func, N, 'list2', func_name, N)

    # output
    record['time'] *= 1000
    record.to_csv(args.out)


if __name__ == '__main__':
    main()
