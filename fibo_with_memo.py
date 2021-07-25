'''
    We are going to time 2 fibonacci functions.
    One with memoization and other doesn't have it.
    '''
import random
import time

n = 40
print("The first {} fibonacci numbers are: \n".format(n))

def fibo(n):
    if n==0: return 0
    if n==1: return 1
    return fibo(n-1) + fibo(n-2)

start = time.time()
for i in range(n):
    print(fibo(i))
end = time.time()
fibo_without_memo = end -start

def fibo_with_memo(n, memo):
    if n<2: return n
    if n in memo: return memo[n]
    memo[n] = fibo_with_memo(n-1, memo) + fibo_with_memo(n-2, memo)
    return memo[n]

start = time.time()
for i in range(n):
    print(fibo_with_memo(i, memo={}))

end = time.time()

fibo_with_memo = end -start
print("Time without memmoization is {} and time with memoization is {}".format(\
        fibo_without_memo, fibo_with_memo))