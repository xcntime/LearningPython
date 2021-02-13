from time import *

def has_duplicates_for(seq):
    for i in range(len(seq)-2):
        for j in range(i+1,len(seq)-1):
            if seq[i]==seq[j]:
                return i
    return  -1

def has_duplicates_list(seq):
    for i in range(len(seq)-2):
        if seq[i] in seq[i+1:]:
            return i
    return  -1

def has_duplicates_dict(seq):
    dct={}
    for i in seq:
        if i in dct:
            return i,True
        else:
            dct[i]=0
    return  -1,False

time_append=0
lst=[]

fin=open("words.txt")
begin_time=time()
for i in fin:
    lst.append(i)
end_time=time()
time_append=end_time-begin_time
print("list append cost time:",time_append,len(lst),lst[:5])
fin.close()

begin_time=time()
has_duplicates_for(lst[:20000])
end_time=time()
print("has_duplicates_for cost time:",end_time-begin_time)

begin_time=time()
has_duplicates_list(lst[:20000])
end_time=time()
print("has_duplicates_list cost time:",end_time-begin_time)

begin_time=time()
has_duplicates_dict(lst[:90000])
end_time=time()
print("has_duplicates_dict cost time:",end_time-begin_time)