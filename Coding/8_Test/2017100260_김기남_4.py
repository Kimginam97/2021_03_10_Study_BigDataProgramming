# 4.자동 판매기 프로그램

# 물건의 가격을 입력
product = input("물건 가격을 입력하시오 : ")

# 입력금액의 갯수
print("=== 입력금액 ===")
won1000Number = input("1000원 지폐 개수: ")
won500Number = input("500원 동전 개수: ")
won100Number = input("100원 동전 개수: ")

# 입력한 금액갯수 * 원가
Won1000 = int(won1000Number)*1000
Won500 = int(won500Number)*500
Won100 = int(won100Number)*100

# 총액에서 뺀 금액
money = Won1000+Won500+Won100
money = int(money)-int(product)

# 거스름돈 500원, 100원 10원 ,1원 구하기
print("=== 거스름돈 ===")
change500 = money // 500  # 몫
money = money % 500  # 나머지
print("500원= ", change500)

change100 = money // 100  # 몫
money = money % 100  # 나머지
print("100원= ", change100)

change10 = money // 10  # 몫
money = money % 10  # 나머지
print("10원= ", change10)

change1 = money // 1  # 몫
print("1원= ", change1)




