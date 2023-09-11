#24262
n = int(input())
print(1)  # 수행횟수
print(0)  # 수행횟수를 다항식으로 나타냈을 때 최고차항의 차수


#24263
n = int(input())
print(n)
print(1)


#24264
n = int(input())
print(n**2)
print(2)


#24265
n = int(input())
print(int(n*(n-1)/2))
print(2)


#24266
n = int(input())
print(n**3)
print(3)


#24267
n = int(input())
print(int(n*(n-1)*(n-2)/6))
print(3)


#24313
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
if (a1*n0 + a0 <= c*n0) and (a1 <= c):   # |a|이기 때문에 a <= c 
    print(1)
else:
    print(0)