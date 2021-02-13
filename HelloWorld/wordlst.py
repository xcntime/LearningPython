from time import *
fin=open("words.txt")

time_append=0
time_plus=0
lst=[]

fin=open("words.txt")
begin_time=time()
for i in fin:
    lst.append(i)
end_time=time()
time_append=end_time-begin_time
print("lst append cost time:",time_append,len(lst),lst[:5])
fin.close()


lst=[]
fin=open("words.txt")
begin_time=time()
for i in fin:
    lst+=[i]
end_time=time()
time_plus=end_time-begin_time
print("lst plus cost time:",time_plus,len(lst),lst[:5])
fin.close()

lst=[]
fin=open("words.txt")
begin_time=time()
for i in fin:
    lst=lst+[i]
end_time=time()
time_plus=end_time-begin_time
print("lst plusV2 cost time:",time_plus,len(lst),lst[:5])
fin.close()

'''
lst append cost time: 0.03126811981201172 113783 ['aa\n', 'aah\n', 'aahed\n', 'aahing\n', 'aahs\n']
lst plus cost time: 0.03124094009399414 113783 ['aa\n', 'aah\n', 'aahed\n', 'aahing\n', 'aahs\n']
lst plusV2 cost time: 32.03929901123047 113783 ['aa\n', 'aah\n', 'aahed\n', 'aahing\n', 'aahs\n']
'''