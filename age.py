cnt=0
me_age=0
mother_age=0
for me_age in range(10,120):
    mother_age = int(str(me_age)[::-1])
    cnt=0
    if mother_age>me_age:
        diff=mother_age-me_age
        cnt = 1
        age=mother_age
        for i in range(me_age+1,120):
            age+=1
            if i==int(str(age)[::-1]) and age-i==diff:
                cnt += 1
                # print(i,age,age-i, cnt)


        if cnt>=6:
            print("cnt:",me_age,mother_age,mother_age-me_age,cnt)
