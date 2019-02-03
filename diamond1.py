if True:
	a=int(input("enter side"))
	k=(2*a)-3
	for i in range(1,(2*a)):
		if i<a+1:
		      print(" "*(a-i),"*",end="")
		      if i>1:
			      print(" "*(2*i-4),"*",end="")
		else:
		      print(" "*(i-a),"*",end="")
		      if i<(2*a)-1:
			      print(" "*(k-3),"*",end="")
		      k=k-2
		print()
