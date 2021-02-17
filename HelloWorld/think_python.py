def read_file(fname):
    lst=[]
    fin=open(fname)
    for line in fin:
        lst.append(line)
    fin.close()
    return lst

def write_file(fname,lst):
    fout=open(fname,'r')
    for line in lst:
        fout.write(line)
    fout.close()
    return len(lst)

def clean_line(lst):
    rst=[]
    for word in lst.split():
        word=word.strip()
        rst.append(word)
    return rst

if __name__ =="__main__":
    pass
