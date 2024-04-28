def test(b):# wrong def test(b=[])
    b.append('a')
    return b
print(test([]))
print(test([]))