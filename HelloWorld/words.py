from time import *
fin =open("words.txt")
cnt=0
cnt_no_e=0

lst=[]
dct={}
for line in fin:
    lst.append(line.strip())
    dct[line.strip()]=0
fin.close()

begin_time=time()
flag= ("zero" in lst)
end_time=time()
print(flag,len(lst),end_time-begin_time)

begin_time=time()
flag= ("zero" in dct)
end_time=time()
print(flag,len(lst),end_time-begin_time)

begin_time=time()
flag=False
for j in lst:
    if j=="zero":
        flag=True

end_time=time()
print(flag,len(lst),end_time-begin_time)