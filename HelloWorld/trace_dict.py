from time import *

l = [(x, x**2) for x in range(2000_0000)]
d = dict(l)

t0 = perf_counter()
for i in d:
    t = i + d[i]
t1 = perf_counter()

for k, v in d.items():
    t = k + v
t2 = perf_counter()

for k in d.keys():
    t = k + d[k]
t3 = perf_counter()

# for k, v in d.iteritems():
#     t = k + v
# t4 = perf_counter()
#
# for k in d.iterkeys():
#     t = k + d[k]
# t5 = perf_counter()
#
# for k, v in zip(d.iterkeys(), d.itervalues()):
#     t = k + v
# t6 = perf_counter()

print("d cost            :",t1-t0)
print("d.item() cost     :",t2-t1)
print("d.keys() cost     :",t3-t2)
# print("d.iteritems() cost :",t4-t3)
# print("d.iterkeys() cost  :",t5-t4)
# print("d.zip(   ) cost    :",t6-t5)