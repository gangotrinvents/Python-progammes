if True:
	str=input("enter string as input")
	l1=list()
	l2=list()
	l=['a','A','e','E','i','I','o','O','u','U']
	for i in range(0,len(str)):
		if str[i] in l:
			k=0
			for j in range(i,len(str)):     #how to print single letter
				l1.insert(k,str[i:j+1])
				k+=1
		else:
			m=0
			for j in range(i,len(str)):     #how to print single letter
				l2.insert(m,str[i:j+1])
				m+=1
	if len(l1)>len(l2):
		print("Kevin ",len(l1))
	elif len(l2)>len(l1):
		print("Stuart ",len(l2))
	else:
		print("Both Kevin and Stuart have same point")
