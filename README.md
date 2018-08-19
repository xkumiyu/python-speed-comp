# Python Speed Comparison

Comparison of processing speed of basic Python functions.

## Result

Basically, data size N = 10^6.

### Standard Input

#### input() vs sys.stdin.readline()

``` python
# input()
N = int(input())
A = [int(input()) for _ in range(N)]
```

``` python
# sys.stdin.readline()
import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|input()|392.40|24.36|
|sys.stdin.readline()|37.09|1.88|

![input vs sys.stdin.readline]("./images/input vs sys.stdin.readline.png")

### Sort

#### sort() vs sorted()

A is a list whose elements are random integer values.

``` python
# sort()
A.sort()
```

``` python
# sorted()
A = sorted(A)
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|sort()|88.54|56.98|
|sorted()|127.03|7.51|

![sort vs sorted]("./images/sort vs sorted.png")

#### key of sort

A is a two-dimensional array whose elements are random integer values.

``` python
# sort, lambda
A.sort(key=lambda x: x[1])
```

``` python
# sort, itemgetter
from operator import itemgetter
A.sort(key=itemgetter(1))
```

``` python
# sorted, lambda
A = sorted(A, key=lambda x: x[1])
```

``` python
# sorted, itemgetter
from operator import itemgetter
A = sorted(A, key=itemgetter(1))
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|sort, lambda|641.17|29.69|
|sort, itemgetter|521.91|4.91|
|sorted, lambda|688.45|35.24|
|sorted, itemgetter|588.17|15.32|

![sort key]("./images/sort key.png")

### Loop

#### for vs while

``` python
# for _ in range(N)
for _ in range(N):
    pass
```

``` python
# for i in range(N)
for i in range(N):
    i
```

``` python
# while i < N
i = 0
while i < N:
    i += 1
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|for _ in range(N)|20.63|0.89|
|for i in range(N)|25.66|0.93|
|while i < N|51.36|1.44|

![for vs while]("./images/for vs while (N = 10^6).png")

### List

#### Initialize the list

``` python
# [None] * N
[None] * N
```

``` python
# [None for _ in range(N)]
[None for _ in range(N)]
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|[None] * N|5.15|0.41|
|[None for _ in range(N)]|41.17|2.05|

![initialize the list]("./images/initialize the list (N = 10^6).png")

#### Refer to in the list

``` python
# for i in range(len(A))
for i in range(len(A)):
    A[i]
```

``` python
# for a in A
for a in A:
    a
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|for i in range(len(A))|41.14|0.56|
|for a in A|11.85|1.51|

![refer to in the list]("/images/refer to in the list (N = 10^6).png")

#### Add to the list

``` python
# append()
A = []
for i in range(N):
    A.append(i)
```

``` python
# A[i] = i
A = [None] * N
for i in range(N):
    A[i] = i
```

``` python
# [i for i in range(N)]
A = [i for i in range(N)]
```

||mean(ms)|std(ms)|
|:-|:-|:-|
|append()|103.99|2.62|
|A[i] = i|70.97|3.93|
|[i for i in range(N)]|65.83|3.20|

![add to the list](/images/add%20to%20the%20list%20(N%20%3D%2010%5E6).png)

## Usage

``` bash
$ python main.py
```
