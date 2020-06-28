def selection(list):
    for i in range(len(list)-1):
        min=i
        for j in range(i+1,len(list)-1):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]
list=[23,11,33,6,3,66]
selection(list)
print(list)