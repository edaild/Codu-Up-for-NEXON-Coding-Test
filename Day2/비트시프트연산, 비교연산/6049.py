# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

#1
a, b = input().split()
a = int(a)
b = int(b)
print(a==b)

#2
a, b= map(int, input().split())
print(a==b)