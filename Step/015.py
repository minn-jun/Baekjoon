# #1934
# import sys
# input = sys.stdin.readline
# t = int(input())
# n = []

# def gcm(x , y):
#     r = x % y
#     if r == 0:
#         return y
#     else:
#         return gcm(y, r)

# for _ in range(t):
#     a, b = map(int, input().split())
#     n.append((a*b)//gcm(a, b))
# for i in n:
#     print(i)


# #13241
# import sys
# input = sys.stdin.readline

# def gcm(x , y):
#     r = x % y
#     if r == 0:
#         return y
#     else:
#         return gcm(y, r)

# a, b = map(int, input().split())
# print((a*b)//gcm(a, b))


# #1735
# import sys
# input = sys.stdin.readline

# def gcm(x , y):
#     r = x % y
#     if r == 0:
#         return y
#     else:
#         return gcm(y, r)
    
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# mo = b * d
# ja = a*d + b*c
# g = gcm(mo, ja)
# mo /= g
# ja /= g
# print(int(ja), int(mo))


# #2485
# import sys
# input = sys.stdin.readline

# def gcm(x , y):
#     r = x % y
#     if r == 0:
#         return y
#     else:
#         return gcm(y, r)
    
# n = int(input())
# tree = []
# cha = []
# cnt = 0
# for _ in range(n):
#     tree.append(int(input()))
# for i in range(n-1):
#     cha.append(tree[i+1]-tree[i])
# a = cha[0]
# for i in cha:
#     a = gcm(a , i)
# for i in cha:
#     cnt += (i//a)-1
# print(cnt)


# #4134
# import sys
# input = sys.stdin.readline

# def isPrime(n):
#     if n == 0 or n == 1:
#         return 2
#     for i in range(2, int(n**(1/2))+1):
#         if n % i == 0:
#             return isPrime(n+1)
#     return n
    
# t = int(input())
# for _ in range(t):
#     print(isPrime(int(input())))


# #1929
# import sys
# input = sys.stdin.readline

# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**(1/2))+1):
#         if n % i == 0:
#             return False
#     return True

# m, n = map(int, input().split())
# for i in range(m, n+1):
#     if isPrime(i) == True:
#         print(i)


# #4948   ## 시간초과
# import sys
# input = sys.stdin.readline

# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**(1/2))+1):
#         if n % i == 0:
#             return False
#     return True

# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         break
#     for i in range(n+1, 2*n+1):
#         if isPrime(i):
#             cnt += 1
#     print(cnt)


#17103
import sys
input = sys.stdin.readline

#13909