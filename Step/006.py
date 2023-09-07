#25083
print(' '*9 + ",r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")


#3003
chess = [1, 1, 2, 2, 2, 8]
w = list(map(int, input().split()))
for i in range(len(chess)):
    print(chess[i]-w[i], end=' ')


#2444
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))


#10988
n = list(input())
m = list(reversed(n))
if n == m:
    print(1)
else:
    print(0)


#1157 ★★★★★ REVIEW
n = input().upper()
n_set = list(set(n))
cnt = []
for i in n_set:
    cnt.append(n.count(i))
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(n_set[cnt.index(max(cnt))])


#2941
cro = ["c=", "c-", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
for i in cro:
    s = s.replace(i, '*')
print(len(s))


#1316
n = int(input())
cnt = n
for i in range(n):
    word = input()
    for a in range(len(word)-1):
        if word[a] == word[a+1]:
            continue
        elif word[a] in word[a+1:]:
            cnt -= 1
            break
print(cnt)

#25206
major = []
allpoint = 0
for i in range(20):
    sub, point, grade = map(str, input().split())
    point = float(point)
    if grade == "A+":
        allpoint += point
        major.append(4.5 * point)
    elif grade == "A0":
        allpoint += point
        major.append(4.0 * point)
    elif grade == "B+":
        allpoint += point
        major.append(3.5 * point)
    elif grade == "B0":
        allpoint += point
        major.append(3.0 * point)
    elif grade == "C+":
        allpoint += point
        major.append(2.5 * point)
    elif grade == "C0":
        allpoint += point
        major.append(2.0 * point)
    elif grade == "D+":
        allpoint += point
        major.append(1.5 * point)
    elif grade == "D0":
        allpoint += point
        major.append(1.0 * point)
    elif grade == "F":
        allpoint += point
        major.append(0 * point)
    else:
        continue
avg = sum(major)/allpoint
print(avg)