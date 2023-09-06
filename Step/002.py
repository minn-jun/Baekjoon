#1330
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')


#9498
score = int(input())
if score >= 90:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')


#2753
year = int(input())
con_1 = (year % 4 == 0) and (year % 100 != 0)
con_2 = year % 400 == 0
if con_1 or con_2:
    print(1)
else:
    print(0)


#14681
x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)


#2884
H, M = map(int, input().split())
if M-45 >= 0:
    M-=45
else:
    M+=15
    H-=1
    if H < 0:
        H+=24
print(H, M)


#2525
a, b = map(int, input().split())
c = int(input())
a+=(c//60)
b+=(c%60)
if b >= 60:
    a+=(b//60)
    b%=60
if a >= 24:
    a-=24
print(a, b)


#2480
a, b, c = map(int, input().split())
if a==b==c:
    money = 10000+a*1000
elif a==b or a==c:
    money = 1000+a*100
elif b==c:
    money = 1000+b*100
else:
    money = max(a, b, c)*100
print(money)