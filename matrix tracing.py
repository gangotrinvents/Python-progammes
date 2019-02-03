a=[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
n=4
start =0
count=0
while(n>0):
    if count%2==0:
        for i in range(start,n):
            start=star
            end=n
            if i==start:
                for j in range(star,end+1):
                    print(a[i][j])
            elif i<n-1:
                print(a[i][end])
            else:
                for j in range(end,star,-1):
                    print(a[i][j]
        count=count+1
    else:
        for i in range(n,start,-1):
            print(a[i][star])
        count=count+1
        n=n-1
        start=start+1
        
        
