a = [1, 2]
b = [1, 3, 5]

a.extend(b)
print(a)

a.extend(a)
print(a)

# 리스트 더하기
a.extend(["a", "b"])
print(a)