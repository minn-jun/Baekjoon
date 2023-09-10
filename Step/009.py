# #5086
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     if a % b == 0:
#         print("multiple")
#     elif b % a == 0:
#         print("factor")
#     else:
#         print("neither")


# #2501
# n, k = map(int, input().split())
# l = []
# for i in range(1, n+1):
#     if n % i == 0:
#         l.append(i)
# if len(l) < k:
#     print(0)
# else:
#     print(l[k-1])


#9506
while True:
    n = int(input())
    a = []
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            a.append(i)    
    if sum(a) == n:
        print(n, '=', end=' ')
        for i in a:
            if i == a[-1]:
                print(i)
            else:
                print(i, end=' + ')
    else:
        print(f"{n} is NOT perfect.")



#1978
#2581
#11653