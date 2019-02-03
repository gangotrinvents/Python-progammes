class student:
    d={}
    def details(self):
        self.d={int(input("enter id")):[input("enter name"),int(input("enter phone number"))]}
    def search(self):
        sear=int(input("enter id to get details"))
        print(self.d[sear])
    def update(self):
        upd=int(input("enter id to get details"))
        l=self.d[upd]
        to_change=int(input("enter 0 to chanege name and 1 to change in name"))
        l[to_change]=input("enter detail")
        self.d[upd]=l
        print(self.d)
s=student()
choice=1
while(choice!=4):
    choice=int(input("enter 1 for detail,2 for search of detail,3 for update ,4 to exit"))
    if choice==1:
        s.details()
        print(s.d)
    elif choice==2:
        s.search()
    elif choice==3:
        s.update()
    else:
        exit
    
