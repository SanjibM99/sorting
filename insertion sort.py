def insertion(list):
    for i in range(1,len(list)):
        current=list[i]
        pos=i
        while pos>0 and list[pos-1]>current:
            list[pos]=list[pos-1]
            pos-=1
            list[pos]=current


list=[33,1,22,2,66,3]
insertion(list)
print(list)