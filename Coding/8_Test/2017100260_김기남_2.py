# 2.자료 비교 프로그램

# 2개의 자료를 입력 받는다
oneData = input("자료 1을 입력하시오 : ").split(",")
twoData = input("자료 2를 입력하시오 : ").split(",")

# 2개의 자료의 중복값을 없애고 값을 오름차순으로 정렬한다
oneResult = sorted(set(oneData))
twoResult = sorted(set(twoData))

print("=== 자료비교 ===")

# 자료1과 자료2의 값이 모두 같은지 검사
if oneResult == twoResult:
    print("2개의 자료구조에 있는 값들이 모두 동일합니다.")
else:
    print("2개의 자료구조에는 다른 값들이 들어있습니다")
