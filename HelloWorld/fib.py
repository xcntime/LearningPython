from time import *
cnt=0
cnt_dct=0
def fib(n):
    global cnt
    cnt+=1

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

dct={0:0,1:1}
def fib_dict(n):
    global cnt_dct
    cnt_dct+=1

    if n in dct:
        return dct[n]
    else:
        dct[n]=rst=fib_dict(n-1)+fib_dict(n-2)
        return fib_dict(n-1)+fib_dict(n-2)

for i in range(30,35):
    begin_time=time()
    rst=fib(i)
    end_time=time()
    print(i,rst,cnt_dct,end_time-begin_time)
    cnt=0

for i in range(2,350):
    begin_time=time()
    rst=fib_dict(i)
    end_time=time()
    print(i,rst,cnt_dct,end_time-begin_time)
    cnt_dct=0
    dct=dct={0:0,1:1}

