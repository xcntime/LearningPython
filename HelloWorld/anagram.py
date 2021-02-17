import think_python as lib
import shelve

def sign(str):
    lst=sorted(list(str))
    rst=''.join(lst)
    return rst

def make_anagrams(fname):
    dct={}
    lst=lib.read_file(fname)
    for line in lst:
        word=line.strip().lower()
        str=sign(word)
        dct.setdefault(str,[]).append(word)
    return dct

def print_anagrams(d):
    for k,v in d.items():
        if len(v)>1:
            print(len(v),k,v)

def print_anagrams_in_order(d):
    lst=[]
    for v in d.values():
        if len(v)>1:
            lst.append((len(v),v))
    lst.sort()

    for i in lst:
        print(i)

def store_anagrams(fname,d):
    shelf=shelve.open(fname,'c')
    for k,v in d.items():
        shelf[k]=v

    shelf.close()

def read_anagrams(fname,word):
    shelf=shelve.open(fname)
    shelf.get(sign(word),[])

if __name__ =="__main__":
    # dct={}
    dct=make_anagrams("words.txt")
    print_anagrams_in_order(dct)
    # store_anagrams("..\..\words_anagrams",dct)


