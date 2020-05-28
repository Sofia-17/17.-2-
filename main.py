#Что больше: сумма элементов последовательности с четными значениями, или с нечетными?
def maxsum(sf):
    try:
        err=0
        sum1=0
        sum0=0
        count0=0
        count1=0
        x=None
        f=open(sf,"r")
        s=None
        for str in f:
            if(s==None):
                try:
                    for sx in [sx for s1 in str.split(' ') for s2 in s1.split('\t') for s3 in s2.split('\n') for sx in s3.split(',') if sx!='']: #строка без всей грязи
                        try:
                            s=int(sx) 
                            if(s%2==0):# если чётная
                                sum0+=s #сумма равна числу
                                count0+=1 # кол-во
                            else:
                                sum1+=s #ан-но для неч
                                count1+=1
                        except:
                                print(sx, ' that word was ingnored')
                except ValueError:
                    err=-1
                    print("Bad first value:", str) #посчитали первый элемент
            else:
                try:
                     for sx in [sx for s1 in str.split(' ') for s2 in s1.split('\t') for s3 in s2.split('\n') for sx in s3.split(',') if sx!='']: # то же самое с остальными элементами
                        try:
                            s=int(sx)
                            if(s%2==0):
                                sum0+=s
                                count0+=1
                            else:
                                sum1+=s
                                count1+=1
                        except:
                            print(sx,' that word was ignored')
                except ValueError:
                    err=-2
                    print("Bad value:", str) #к первому элементу прибавляю последующие

        if(count1==0 or count0==0):
            x=-1 
        elif(sum0==sum1):
            x=0
        elif(sum0>sum1):
            x=1
        elif(sum0<sum1):
            x=2
        f.close()
        return err,x
    except FileNotFoundError:
        err=-3
        print("Can't open file")
    return -1,-1

err,x=maxsum("in.txt")
if(err<0):
    print("Error")
elif(x==-1):
    print("Четных либо нечетных чисел в последовательности нет")
elif(x==0):
    print("Суммы четных и нечетных равны")
elif(x==1):
    print("Сумма четных больше")
elif(x==2):
    print("Сумма нечетных больше")
