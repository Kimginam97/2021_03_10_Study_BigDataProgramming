print('Hello')

a = input("값을 입력하세요: ")

# 문자열 안에서 \n 기호 사용하기
print("안녕하세요 \n 저는 3학년 C반 김기남 \n 입니다")


# 문자열 안에 따옴표는 다른따옴표로 둘러싼다
print("안녕하세요 '김기남' 입니다 ")


# 자료형 확인
b = type(123)
c = type(-3.13)

print(b)
print(c)

# 자료형 변환 (실수)
d = float(3)
e = float("12345")

print(d)
print(e)

# 자료형 변환 (문자열)
string = str(3.15)
print(string)

# 자료형 변환 (논리형)
helloBoolean = bool("asdasd")
print(helloBoolean)

helloBoolean1 = bool("")
print(helloBoolean1)