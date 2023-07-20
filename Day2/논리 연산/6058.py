# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자. 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

a,b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not c and not d)