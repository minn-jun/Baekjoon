#2739
n = int(input())
for i in range(1, 10):
    print(f"{n} * {i} = {n*i}")


#10950
t = int(input())
s = []
for i in range(t):
    a ,b = map(int, input().split())
    s.append(a+b)
for j in s:
    print(j)

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print(A + B)


#8393
n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)


#25304
pay = int(input())
n = int(input())
total = 0
for i in range(n):
    a, b = map(int, input().split())
    total += (a*b)
if total == pay:
    print("Yes")
else:
    print("No")


#25314
n = int(input())
byte = n//4
for i in range(byte):
    print("long", end=' ')
print("int")


#15552
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())  
    print(a+b)


#11021
t = int(input())
cs = []
for i in range(t):
    a, b = map(int, input().split())
    cs.append(a+b)
for j in range(1, t+1):
    print(f"Case #{j}: {cs[j-1]}")


#11022
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")


#2438
n = int(input())
for i in range(n):
    print('*' * (i+1))


#2439
n = int(input())
for i in range(n):
    print(' ' * (n-1-i) + '*' * (i+1))


#10952
while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    print(a+b)

#10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break