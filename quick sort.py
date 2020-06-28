def partition(list,first,last):
	pivot=list[first]
	left=first
	right=last
	while True:
		while left<=right and list[left]<=pivot:
			left+=1
		while left<=right and list[right]>=pivot:
			right-=1
		if right<left:
			break
		else:
			list[left],list[right]=list[right],list[left]
	list[first],list[right]=list[right],list[first]
	return right	
	
def quick(list,first,last):
	if first<last:
		p=partition(list,first,last)
		quick(list,first,p-1)
		quick(list,p+1,last)

list=[12,11,3,122,56,2,45]
n=len(list)
quick(list,0,n-1)
print(list)
