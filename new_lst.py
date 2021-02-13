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
print("lst append cost time:",time_append,len(lst))
fin.close()

lst=[]
fin=open("words.txt")
begin_time=time()
for i in fin:
    lst+=[i]
end_time=time()
time_plus=end_time-begin_time
print("lst append cost time:",time_plus,len(lst))
fin.close()