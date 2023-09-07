# #25083
# print(' '*9 + ",r'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")


# #3003
# chess = [1, 1, 2, 2, 2, 8]
# w = list(map(int, input().split()))
# for i in range(len(chess)):
#     print(chess[i]-w[i], end=' ')


# #2444
# n = int(input())
# for i in range(1, n+1):
#     print(' '*(n-i) + '*'*(2*i-1))
# for i in range(n-1, 0, -1):
#     print(' '*(n-i) + '*'*(2*i-1))


# #10988
# n = list(input())
# m = list(reversed(n))
# if n == m:
#     print(1)
# else:
#     print(0)


# #1157 ★★★★★ 복습
# n = input().upper()
# n_set = list(set(n))
# cnt = []
# for i in n_set:
#     cnt.append(n.count(i))
# if cnt.count(max(cnt)) >= 2:
#     print('?')
# else:
#     print(n_set[cnt.index(max(cnt))])


#2941
#1316
#25206