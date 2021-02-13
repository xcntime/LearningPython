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
    print("a1=", a1, id(a1))
    print("a2=", a2, id(a2))
    print("a3=", a3, id(a3))
    print("a4=", a4, id(a4))
    print("=============End the fun V1===========")

def test_local_v2():
    print("=============In the fun V2===========")
    #a1 = a1 + 100  #运行错误，故注释之
    #a3.append(333)
    a1 = 100
    a2 = "ijkl"
    a3 = [18, 19, 20]
    a3.append("local")

    a4[0] = 100
    a4.append(888)
    print("a1=", a1, id(a1))
    print("a2=", a2, id(a2))
    print("a3=", a3, id(a3))
    print("a4=", a4, id(a4))
    print("=============End the fun V2===========")


test_global_v1()
test_local_v2()

print("a1=", a1, id(a1))
print("a2=", a2, id(a2))
print("a3=", a3, id(a3))
print("a4=", a4, id(a4))
