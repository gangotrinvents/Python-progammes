a=input("enter sides")
b=list(a)
temp=max(b)
e=len(b)
count=0
while(len(b)):                           #35153
    print("loop start")
    print(len(b),"----")           #5>1
    if e>1:
            
        if (len(b)>1):
            print("if stat 1")
            if (b[0]>=b[len(b)-1]) and (b[0]<=temp):
                print("if stat 2")
                temp=b[0]
                print(temp)
                b.pop(0)
            elif (b[len(b)-1]>=b[0]) and (b[len(b)-1]<=temp):
                print("if stat 3")
                temp=b[len(b)-1]
                print(temp)
                b.pop(len(b)-1)
            else:
                print("no")
                print("inside")
                count=1
                break
        elif (b[0]>temp):
            print("outer")
            count=1
            b.pop(0)
            print("no")
            break
        else:
            b.pop(0)
            break
    else:
        print("enter more than 1 sides to change becoz one side eill oobvious to be stacked")
        break   
if count==0:
    print("yes")
