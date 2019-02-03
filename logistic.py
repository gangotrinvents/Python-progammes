
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)
data,x,y,alpha,theta,label,one,p,k=None,None,None,None,None,None,None,None,None

def data_preprocessing():
    global data,x,y,one,p,alpha,theta,label,k
    data=pd.read_csv("Iris.csv")
    data.dropna()
    x=np.array(data.iloc[:,:-1])
    label=[]
    temp=data["Species"]
    k=np.array(temp)
    for i in k:
        if(i=="Iris-setosa"):
            label.append([1,0,0])
        elif(i=="Iris-versicolor"):
            label.append([0,1,0])
        else:
            label.append([0,0,1])
                
    one=np.ones((x.shape[0],1))
    #x=np.concatenate((one,x),axis=1) 
    y=np.array(label)   
    p=np.random.permutation(len(x))
    x=x[p]
    y=y[p]
    alpha=0.0001
    theta=np.random.randn(x.shape[1],3)*0.01



def cost(x,y,theta):
    h1=np.matmul(x,theta)
    sig=1/(1+np.exp(-h1))
    c1= (-1/x.shape[0])*np.sum(y*np.log(sig)+(1-y)*(np.log(1-sig)))
    return h1,c1

def gradient_descent(x,y):
    global theta
    iter=10900
    
    for i in range(iter):
        h2,c2=cost(x,y,theta)
        theta=theta- (alpha/x.shape[0])*(np.matmul(x.T,(h2-y)))
        
        if (i%100)==0:
            print(c2)
            
data_preprocessing()
gradient_descent(x,y)
pred=x@theta
correct=0
for i in range(x.shape[0]):
    k1=np.argmax(y[i])
    k2=np.argmax(pred[i])
    if(k1==k2):
        correct+=1
print(correct/x.shape[0])
