def display(l,n):
	for i in range(n):
		print(l[i],end='\t')

n = int(input('Enter no of elements : '))
l = list(map(int,input('Enter the values : ').split()))[:n]
display(l,n)