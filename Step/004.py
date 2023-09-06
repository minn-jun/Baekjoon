#10807
n = int(input())
l = list(map(int, input().split()))
v = int(input())
print(l.count(v))


#10871
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    if x > i:
        print(i, end=' ')


#10818
n = int(input())
l = list(map(int, input().split()))
print(min(l), max(l))


#2562
# l = []
# for i in range(9):
#     l.append(int(input()))

l = [int(input()) for i in range(9)]  # 한 줄 for
print(max(l))
print(l.index(max(l))+1)


#10810
n, m = map(int, input().split())
l = [0]*n
for a in range(m):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        l[b] = k
for c in l:
    print(c, end=' ')


#10813
n, m = map(int, input().split())
l = [i+1 for i in range(n)]
for a in range(m):
    i, j = map(int, input().split())
    temp = l[i-1]
    l[i-1] = l[j-1]
    l[j-1] = temp
for b in l:
    print(b, end=' ')


# #5597
student = [i+1 for i in range(30)]
for i in range(28):
    a = int(input())
    if a in student:
        student.remove(a)
for i in range(2):
    print(student[i])


#3052
a = []
for i in range(10):
    a.append(int(input()) % 42)
b = set(a)
print(len(b))

# a = [int(input())%42 for i in range(10)]
# print(len(set(a)))


#10811
n, m = map(int, input().split())
l = [x+1 for x in range(n)]
for a in range(m):
    i, j = map(int, input().split())
    temp = l[i-1:j]
    temp.reverse()
    l[i-1:j] = temp
for b in l:
    print(b, end=' ')


#1546
n = int(input())
score = list(map(int, input().split()))
m = max(score)
new_s = [i/m*100 for i in score]
avg = sum(new_s)/n
print(avg)