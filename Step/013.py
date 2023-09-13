# #2750
# n = int(input())
# num = []
# for i in range(n):
#     num.append(int(input()))
# num = sorted(num)
# for i in num:
#     print(i)

# n = int(input())
# num = []
# for i in range(n):
#     num.append(int(input()))
# for i in range(n):
#     for j in range(i+1, n):
#         if num[i] > num[j]:
#             num[i], num[j] = num[j], num[i]
# for i in num:
#     print(i)


# #2587
# num = []
# for i in range(5):
#     num.append(int(input()))
# print(int(sum(num)/5))
# print(sorted(num)[2])


# #25305
# n, k = map(int, input().split())
# score = list(map(int, input().split()))
# s = list(reversed(sorted(score)))
# print(s[k-1])


# #2751
# import sys
# n = int(sys.stdin.readline())
# num = []
# for i in range(n):
#     num.append(int(sys.stdin.readline()))
# for i in sorted(num):
#     print(i)


#10989


# #1427
# n = input()
# l = []
# for i in n:
#     l.append(i)
# l = list(reversed(sorted(l)))
# print("".join(l))


# #11650
# import sys
# n = int(sys.stdin.readline())
# a = []
# for _ in range(n):
#     a.append(list(map(int, sys.stdin.readline().split())))
# a = sorted(a)
# for i in range(n):
#     print(a[i][0], a[i][1])


# #11651
# import sys
# n = int(sys.stdin.readline())
# a = []
# for _ in range(n):
#     a.append(list(map(int, sys.stdin.readline().split())))
# for i in range(n):
#     a[i][0], a[i][1] = a[i][1], a[i][0]
# a = sorted(a)
# for i in range(n):
#     a[i][0], a[i][1] = a[i][1], a[i][0]
#     print(a[i][0], a[i][1])


# #1181
# import sys
# n = int(sys.stdin.readline())
# word = []
# for _ in range(n):
#     word.append(sys.stdin.readline().strip())
# word = list(set(word))
# word.sort()
# word.sort(key=len)
# for i in word:
#     print(i)


# #10814
# import sys
# n = int(sys.stdin.readline())
# p = []
# for _ in range(n):
#     p.append(list(sys.stdin.readline().split()))
# p.sort(key=lambda a : int(a[0]))
# for i in range(n):
#     print(p[i][0], p[i][1])


# #18870
# import sys
# n = int(sys.stdin.readline())
# l1 = list(map(int, sys.stdin.readline().split()))
# l2 = list(sorted(set(l1)))
# dic = {l2[i]:i for i in range(len(l2))}
# for i in l1:
#     print(dic[i], end=' ')