# #2798
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# s =[]
# for i in range(0, n):
#     for j in range(i+1, n):
#         for k in  range(j+1, n):
#             if num[i]+num[j]+num[k] <= m:
#                 s.append(num[i]+num[j]+num[k])
# print(max(s))


# #2231
# n = int(input())
# m =[]
# for i in range(1, n):
#     s = 0
#     for j in range(len(str(i))):
#         s += (i//(10**j))%10
#     s += i
#     if s == n:
#         m.append(i)
# if len(m) == 0:
#     print(0)
# else:
#     print(min(m))


# #19532
# a, b, c, d, e, f = map(int, input().split())
# if a*e-b*d != 0 and a != 0:
#     y = (a*f-c*d)/(a*e-b*d)
#     x = (c-b*y)/a
# elif a == 0 and b != 0 and d != 0:
#     y = c/b
#     x = (f-c*e/b)/d
# elif a != 0 and b == 0 and e != 0:
#     x = c/a
#     y = (f-c*d/a)/e
# print(int(x), int(y))


#1018
n, m = map(int, input().split())
b = []


# #1436
# n = int(input())
# num = []
# i = 666
# while len(num) < n:
#     if "666" in str(i):
#         num.append(i)
#     i += 1
# print(num[n-1])


#2839
n = int(input())


while True:
    pass