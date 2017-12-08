import copy
a = [[[1, 2], 1], [[1, 2], 1], [[1, 2], 1]]
p = {"nombre": 2}
b = [i[0] for i in a]
b[0] = 0
for d in p.items():
    print(d[0], d[1])
d = "{0:.3f}".format(5.1234554321)
print(d)
