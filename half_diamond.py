
a=int(input("enter side"))
k=1
for i in range(1,(2*a)):
    if i<a+1:
              print("  "*(a-i),end="")
              for j in range((a+1)-i,a+1):
                  if i%2==0:
                      if j%2==0:
                          print("%2d"%j,end="")
                      else:
                          print("  ",end="")
                  else:
                      if j%2!=0:
                          print("%2d"%j,end="")
                      else:
                          print("  ",end="")
    else:
        print("  "*k,end="")
        for j in range(i-(a-1),a+1):
            if i%2==0:
                if j%2==0:
                    print("%2d"%j,end="")
                else:
                    print("  ",end="")
            else:
                if j%2!=0:
                    print("%2d"%j,end="")
                else:
                    print("  ",end="")
        k=k+1
    print("")

    
      
      
		
		      
