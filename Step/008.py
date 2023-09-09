# #2745
# n, b = map(str, input().split())
# print(int(n, int(b)))

# n, b = map(str, input().split())
# b = int(b)
# l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16,
#        'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23,
#        'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30,
#        'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
# num = 0
# for i in range(len(n)):
#     if n[len(n)-1-i] in l:
#         num += int(n[len(n)-1-i]) * pow(b, i)
#     else:
#         num += dic.get(f'{n[len(n)-1-i]}') * pow(b, i)
# print(num)


# #11005
# n, b = map(int, input().split())
# num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# l = []
# while n//b != 0:
#     l.insert(0, n%b)
#     n = n//b
# l.insert(0, n%b)
# for i in l:
#     print(num[i], end='')


# #2720
# t = int(input())
# for i in range(t):
#     c = int(input())
#     q = c//25
#     d = (c%25)//10
#     n = ((c%25)%10)//5
#     p = ((c%25)%10)%5
#     print(q, d, n, p)


# #2903
# n = int(input())
# print((1+2**n)**2)


#2292


# #1193
# x = int(input())
# y = x
# line = 1
# while x > line:
#     x -= line
#     line += 1
# idx = int(y - (line*(line-1)/2))
# if line % 2 == 0:
#     a = idx
#     b = line-idx+1
# elif line % 2 != 0:
#     a = line-idx+1
#     b = idx
# print(f"{a}/{b}")


# #2869
# a, b, v = map(int, input().split())
# d = (v-b)/(a-b)
# if int(d) == d:
#     print(int(d))
# else:
#     print(int(d)+1)