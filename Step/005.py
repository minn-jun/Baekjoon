#27866
s = input()
i = int(input())
print(s[i-1])


#2743
print(len(input()))


#9086
t = int(input())
for i in range(t):
    s = input()
    print(f"{s[0]}{s[-1]}")


#11654
c = input()
print(ord(c))
# ord() >> 문자를 아스키코드로
# chr() >> 아스키코드를 문자로


#11720
n = int(input())
print(sum(list(map(int, input()))))


#10809
# from string import ascii_lowercase 
# alphabet = list(ascii_lowercase)   # 알파벳 리스트 생성
s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')


#2675
t = int(input())
for i in range(t):
    r, s = map(str, input().split())
    for j in range(len(s)):
        print(s[j]*int(r), end='')
    print()


#1152
s = input()
print(len(s.split()))


#2908
a, b = map(list, input().split())
a[0], a[2] = a[2], a[0]
b[0], b[2] = b[2], b[0]
a = int(''.join(a))
b = int(''.join(b))
if a > b:
    print(a)
elif a < b:
    print(b)


#5622
word = input()
a = ['A', 'B', 'C', 3]
d = ['D', 'E', 'F', 4]
g = ['G', 'H', 'I', 5]
j = ['J', 'K', 'L', 6]
m = ['M', 'N', 'O', 7]
p = ['P', 'Q', 'R', 'S', 8]
t = ['T', 'U', 'V', 9]
w = ['W', 'X', 'Y', 'Z', 10]
num = [a, d, g, j, m, p, t, w]
time = 0
for x in word:
    for y in num:
        if x in y:
            time += y[-1]
print(time)


#11718
while True:
    try:
        print(input())
    except:
        break

# s = []
# while True:
#     try:
#         a = input()
#         if a != '':
#             s.append(a)
#         else:
#             break
#     except:
#         break
# for i in s:
#     print(i)