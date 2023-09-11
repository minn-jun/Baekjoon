#5086
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")


#2501
n, k = map(int, input().split())
l = []
for i in range(1, n+1):
    if n % i == 0:
        l.append(i)
if len(l) < k:
    print(0)
else:
    print(l[k-1])


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
n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in l:
    a = []
    for j in range(1, i+1):
        if i % j == 0:
            a.append(j)
    if len(a) == 2:
        cnt += 1
print(cnt)


#2581
# m = int(input())
# n = int(input())
# l = []
# for i in range(m, n+1):
#     a = []
#     for j in range(1, i+1):
#         if i % j == 0:
#             a.append(j)
#     if len(a) == 2:
#         l.append(a[1])
# if len(l) == 0:
#     print(-1)
# else:
#     print(sum(l))
#     print(l[0])

m = int(input())
n = int(input())
if m == 1:
    m += 1
cnt = [c for c in range(m, n+1)]
for i in range(m, n+1):
    for j in range(2, i):
        if i % j == 0:
            cnt.remove(i)
            break
if len(cnt) == 0:
    print(-1)
else:
    print(sum(cnt))
    print(cnt[0])


#11653
n = int(input())
i = 2
while True:
    if n == 1:
        break
    if n % i == 0:
        print(i)
        n /= i
    else:
        i += 1