# 1.평균 계산 프로그램

# 국어, 수학, 영어 점수 입력
ko = input("국어 점수를 입력하시오 : ")
math = input("수학 점수를 입력하시오 : ")
en = input("영어 점수를 입력하시오 : ")

# 국어, 수학, 영어 실수로 형변환
result_ko = float(ko)
result_math = float(math)
result_en = float(en)

# 국어, 수학, 영어 총점수
total = (result_ko+result_math+result_en)

# 국어, 수학, 영어 평균
average = (total/3)

# 0~100점 사이의 범위
if (0 < result_ko <= 100) and (0 < result_math <= 100) and (0 < result_en <= 100):
    print('=== 평균계산 ===')
    print('평균= ', average)
else:
    print('0~100점 사이의 범위만 입력이 가능합니다')

