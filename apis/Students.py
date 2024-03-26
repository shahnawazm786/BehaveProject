def abc(x, y):
    if(isinstance(x,str) or isinstance(y,str)):
        print("%s %s"%(x,y))

    else:
        print(x+y)


abc(10,5)
