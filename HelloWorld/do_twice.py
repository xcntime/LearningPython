def do_twice(func,var):
    func(var)
    func(var)

def rfill(str,width,chr):
    print(chr*(width-len(str)),str)

do_twice(print,"aa")
rfill("hello,world!",5,' ')