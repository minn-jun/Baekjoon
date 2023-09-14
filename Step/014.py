# #10815
# import sys
# n = int(sys.stdin.readline())
# nl = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# ml = list(map(int, sys.stdin.readline().split()))
# dic = {i : 1 for i in nl}
# for i in ml:
#     if i in dic:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


# #14425
# import sys
# n, m = map(int, sys.stdin.readline().split())
# s = []
# count = 0
# for _ in range(n):
#     s.append(sys.stdin.readline().strip())
# s = set(s)
# for _ in range(m):
#     st = sys.stdin.readline().strip()
#     if st in s:
#         count += 1
# print(count)


# #7785
# import sys
# n = int(sys.stdin.readline())
# p = set()
# for _ in range(n):
#     name, log = map(str, sys.stdin.readline().strip().split())
#     if log == "enter":
#         p.add(name)
#     elif log == "leave":
#         p.remove(name)
# for i in list(reversed(sorted(p))):
#     print(i)


# #1620
# import sys
# n, m = map(int, sys.stdin.readline().split())
# num_dic = {}
# name_dic = {}
# for i in range(1, n+1):
#     a = sys.stdin.readline().strip()
#     num_dic[str(i)] = a
#     name_dic[a] = str(i)
# answer = []
# for i in range(m):
#     answer.append(sys.stdin.readline().strip())
# for i in answer:
#     if i in num_dic:
#         print(num_dic[i])
#     elif i in name_dic:
#         print(name_dic[i])


#10816
import sys
n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))
dic = {i : 1 for i in nl}


# #1764
# import sys
# n, m = map(int, sys.stdin.readline().split())
# h = set()
# l = set()
# for _ in range(n):
#     h.add(sys.stdin.readline().strip())
# for _ in range(m):
#     l.add(sys.stdin.readline().strip())
# hl = h & l
# print(len(hl))
# for i in sorted(hl):
#     print(i)


# #1269
# import sys
# a, b = map(int, sys.stdin.readline().split())
# A = set(map(int, sys.stdin.readline().strip().split()))
# B = set(map(int, sys.stdin.readline().strip().split()))
# print(len(A-B) + len(B-A))


# #11478
# import sys
# s = sys.stdin.readline().strip()
# l = len(s)
# a = set()
# for i in range(l):
#     for j in range(i+1, l+1):
#         a.add(s[i:j])
# print(len(a))