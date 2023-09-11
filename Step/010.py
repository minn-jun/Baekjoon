#27323
a = int(input())
b = int(input())
print(a*b)


#1085
x, y, w, h = map(int, input().split())
l = [x, y, w-x, h-y]
print(min(l))


#3009
a = []
b = []
for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
for i in range(3):
    if a.count(a[i]) == 1:
        x1 = a[i]
    if b.count(b[i]) == 1:
        y1 = b[i]
print(x1, y1)


#15894
print(int(input())*4)


#9063
import sys
n = int(sys.stdin.readline())
a = []
b = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)
print((max(a)-min(a))*(max(b)-min(b)))


#10101
a = []
for i in range(3):
    a.append(int(input()))
if sum(a) == 180:
    if a[0] == 60 and a[1] == 60 and a[2] == 60:
        print("Equilateral")
    elif a[0]==a[1] or a[1]==a[2] or a[0]==a[2]:
        print("Isosceles")
    elif a[0] != a[1] != a[2]:
        print("Scalene")
else:
    print("Error")


#5073
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if max(a,b,c) >= (a+b+c) - max(a,b,c):
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a==b or b==c or c==a:
            print("Isosceles")
        elif a != b != c:
            print("Scalene")


#14215
l = list(map(int, input().split()))
m = l.index(max(l))
while l[m] >= sum(l) - l[m]:
    l[m] -= 1
print(sum(l))