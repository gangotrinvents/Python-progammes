class add:
    def fun1(self,a):
        global c
        self.c=a
    def add1(self,*b):
        print(c)
        result=0
        result=c+b.c
        return result
if __name__=='__main__':
    obj1=add()
    obj2=add()
    obj1.fun1(12)
    obj2.fun1(15)
    print(obj1.c,obj2.c)
    obj1.add1(obj2)
print(result)
