import sys
a = 0
b = True
c = 2
d = 1.1
e =""
f = []
g =()
h = {}
i = set([])

# print(" %s size is %d ,addr:%d"%(type(a),sys.getsizeof(a), id(a)) )
# print(" %s size is %d ,addr:%d"%(type(b),sys.getsizeof(b), id(b)) )
# print(" %s size is %d ,addr:%d"%(type(c),sys.getsizeof(c), id(c)) )
# print(" %s size is %d ,addr:%d"%(type(d),sys.getsizeof(d), id(d)) )
# print(" %s size is %d ,addr:%d"%(type(e),sys.getsizeof(e), id(e)) )
# print(" %s size is %d ,addr:%d"%(type(f),sys.getsizeof(f), id(f)) )
# print(" %s size is %d ,addr:%d"%(type(g),sys.getsizeof(g), id(g)) )
# print(" %s size is %d ,addr:%d"%(type(h),sys.getsizeof(h), id(h)) )
# print(" %s size is %d ,addr:%d"%(type(i),sys.getsizeof(i), id(i)) )


 # <type 'int'> size is 12
 # <type 'bool'> size is 12
 # <type 'long'> size is 14
 # <type 'float'> size is 16
 # <type 'str'> size is 21
 # <type 'list'> size is 36
 # <type 'tuple'> size is 28
 # <type 'dict'> size is 140
 # <type 'set'> size is 116

print(" {0} size is {1} ,addr:{2}".format(type(a),sys.getsizeof(a), id(a)) )
print(" {0} size is {1} ,addr:{2}".format(type(b),sys.getsizeof(b), id(b)) )
print(" {0} size is {1} ,addr:{2}".format(type(c),sys.getsizeof(c), id(c)) )
print(" {0} size is {1} ,addr:{2}".format(type(d),sys.getsizeof(d), id(d)) )
print(" {0} size is {1} ,addr:{2}".format(type(e),sys.getsizeof(e), id(e)) )
print(" {0} size is {1} ,addr:{2}".format(type(f),sys.getsizeof(f), id(f)) )
print(" {0} size is {1} ,addr:{2}".format(type(g),sys.getsizeof(g), id(g)) )
print(" {0} size is {1} ,addr:{2}".format(type(h),sys.getsizeof(h), id(h)) )
print(" {0} size is {1} ,addr:{2}".format(type(i),sys.getsizeof(i), id(i)) )