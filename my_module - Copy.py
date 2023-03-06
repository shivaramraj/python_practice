def add(*args):
    a=0
    for x in args:
        #print(x)
        a+=x
    return(a)
if __name__=='__main__':
    print(add(1,2,3,4))
