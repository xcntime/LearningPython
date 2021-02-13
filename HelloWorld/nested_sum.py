dep_cnt=0
lst_dst=[]
def nested_sum(lst):
    global dep_cnt
    sum=0
    dep_cnt+=1

    for i in lst:
        if isinstance(i,int):
            sum+=i
            if dep_cnt==1:
                lst_dst.append(sum)
        elif type(i) ==type([]):
            sum+=nested_sum(i)
            dep_cnt -= 1
            if dep_cnt<=1:
                lst_dst.append(sum)
        else:
            print(type(i),type(type(i)))

    return sum

lst_src = []
lst_dst = []
lst_tmp = []
info = "abcdefghijklmnopqrsruvwxyz"

for i in range(1, 6):
    lst_src.append(i * 2)
    lst_dst += [lst_src[-1]]
    lst_dst.insert(0, i * 2 - 1)

lst_dst.insert(-i+i, i * 2)
lst_tmp = lst_dst[i:i+3:3]+sorted(lst_dst)
print("lst_src:", lst_src, '\nlst_dst:', lst_dst, '\nlst_tmp:', lst_tmp)
print(sum(lst_dst), len(lst_dst), max(lst_dst), min(lst_dst), '\n')

del lst_tmp[0]
t = lst_tmp.pop(-1)
lst_dst.remove(i * 2)
lst_dst.sort()
lst_dst =lst_dst+ list(info)[0:10:2]
lst_dst.append(''.join(lst_dst[2*i:]))
lst_tmp.append(lst_dst[0:2*i])
lst_tmp[-1].append(lst_dst[0:2*i])


print("lst_src:", lst_src, '\nlst_dst:', lst_dst, '\nlst_tmp:', lst_tmp)
print(nested_sum(lst_tmp))
print("lst_src:", lst_src, '\nlst_dst:', lst_dst, '\nlst_tmp:', lst_tmp)
