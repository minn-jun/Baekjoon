#2738
n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    A.append(list(map(int, input().split())))
for j in range(n):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j], end=' ')
    print()


#2566
num = []
max_n = 0
for i in range(9):
    num.append(list(map(int, input().split())))
for i in range(len(num)):
    for j in range(len(num[0])):
        if num[i][j] > max_n:
            max_n = num[i][j]
        else:
            continue
for i in range(len(num)):
    for j in range(len(num[0])):
        if num[i][j] == max_n:
            print(max_n)
            print(i+1, j+1)
            break


#10798
w = []
length = 0
for i in range(5):
    w.append(list(map(str, input())))
for i in w:
    if len(i) > length:
        length = len(i)
for i in w:
    if len(i) != length:
        i += '_'*(length-len(i))
for i in range(length):
    for j in range(len(w)):
        if w[j][i] == '_':
            continue
        else:
            print(w[j][i], end='')

# w = [input() for i in range(5)]
# for i in range(15):
#     for j in range(5):
#         try:
#             print(w[j][i], end='')
#         except IndexError:
#             continue


#2563
n = int(input())
paper = [[0 for i in range(101)] for j in range(101)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            paper[x+j][y+k] = 1
count = 0
for i in range(100):
    count += paper[i].count(1)
print(count)
