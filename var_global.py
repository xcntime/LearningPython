a1 = 1
a2 = "ab"
a3 = [11, 12, 13]
a4 = [21, 22, 23, [24, 25, 26]]

print("a1=", a1, id(a1))
print("a2=", a2, id(a2))
print("a3=", a3, id(a3))
print("a4=", a4, id(a4))


def test_global_v1():
    print("=============In the fun V1===========")
    a3[0] = 100
    a3.append(888)
    print("a1=", a1, id(a1))
    print("a2=", a2, id(a2))
    print("a3=", a3, id(a3))
    print("a4=", a4, id(a4))
    print("=============End the fun V1===========")


def test_global_v2(a1, a2, a3, a4):
    print("=============In the fun V2===========")
    a1 = a1 + 10
    a2 = "efgh"
    a3 = [15, 16, 17]

    a4 = a4[0:]
    a4.append(88)
    print("a1=", a1, id(a1))
    print("a2=", a2, id(a2))
    print("a3=", a3, id(a3))
    print("a4=", a4, id(a4))
    print("=============End the fun V2===========")


def test_global_v3():
    print("=============In the fun V3===========")
    #a1 = a1 + 100  #运行错误，故注释之
    #a3.append(333)
    a1 = 100
    a2 = "ijkl"
    a3 = [18, 19, 20]

    a4 = a3
    a3.append(333)
    print("a1=", a1, id(a1))
    print("a2=", a2, id(a2))
    print("a3=", a3, id(a3))
    print("a4=", a4, id(a4))
    print("=============End the fun V3===========")


test_global_v1()
test_global_v2(0.1, "v1", [1,2,3], [100,101,102,[201,202,203]])
test_global_v3()

print("a1=", a1, id(a1))
print("a2=", a2, id(a2))
print("a3=", a3, id(a3))
print("a4=", a4, id(a4))
