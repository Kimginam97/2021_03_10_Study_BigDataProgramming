# a = [(1, 2), (3, 4)]
#
# for i, j in a:
#     print(j)


# a = [1, 2, 3]
# i = 0
#
# while i < len(a):
#     print(a[i])
#     i += 1


# t = ("a", "b", "c", "d", "e")
# s = ""
#
# for c in t:
#     s += c
# else:
#     print(s)

# a = list(range(3))
#
# print(a)

def test(a, *b):
    return a - b[-1]


print(test(1, 2))
