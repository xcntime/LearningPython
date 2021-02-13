def is_reverse(word):
    return word==word[::-1]

flag=False

def is_hw(meter,start,length):
    meter=str(meter)[start:start+length]
    if flag==True:
        # print(meter)
        pass
    return meter==meter[::-1]
i=100000
while i <1000000:
    if is_hw(i,2,4) and is_hw(i+1,1,5) and is_hw(i+2,1,4) and is_hw(i+3,0,6):
        flag=True
        is_hw(i,2,4)
        print(i)
    else:
        flag=False
    i+=1

print("goodbye")