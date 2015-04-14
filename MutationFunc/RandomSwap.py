'''
Created on Mar 23, 2015

@author: pengjie137
'''
import random
from datetime import datetime
import time
import math
from code.prefreaders import SushiPref
from code.prefUtil import SushiPrefUtil

class Mutation(object):
    '''
    classdocs
    '''

    entry = None
    degree=0.5
    def __init__(self, entry,degree):
        '''
        Constructor
        '''
        self.entry=entry;
        self.degree=degree
        
    def LoadPref(self):
        
        self.raw_pref = SushiPref(self.prefpath)
        self.raw_pref.loadUp()
    
    def randomSwap(self):
        random.seed(datetime.now())
        if(random.random()<self.degree):
            random.shuffle(self.entry)
    
    def normalNoise(self,degree):
        #dic={0:self.entry[0],1:self.entry[1],2:self.entry[2],3:self.entry[3],4:self.entry[4],5:self.entry[5],6:self.entry[6],7:self.entry[7],8:self.entry[8],9:self.entry[9]}       
        l=self.entry.tolist()              
        for index in range(0,10):
            random.seed(time.time())
            tem=0
            if(random.random()<2*degree*self.gaussianFunc(index)):
                random.seed(time.time())                
                tem=random.randint(0,9)                                                                
                ori=l[index]
                l[index]=tem
                i=self.entry.tolist().index(ori)
                l[i]=ori   
        for index in range(0,10): 
            self.entry[index]=l[index];
        #list.sort(self.entry.tolist(),key=lambda k: self.entry[k]);
    
    def check(self,l): 
        for index in range(0,10):
            if(l.count(l[index])>1):
                return False
        return True
    
    def find(self,l,v): 
        for index in range(0,10):
            if(l[index]==v):
                return int(index)      
    def gaussianFunc(self,index):
        x=(index-5.5)*4/9
        y=math.exp(-x*x/2)/math.sqrt(2*math.pi)
        return y   
    
    def poissonFunc(self,index,degree):
        f = lambda self, n: n==0 and 1 or n*self(self, n-1)
        sum=0
        for i in range(0,index+1):
            sum=math.pow(degree, i)/f(f,i)        
        y=math.exp(-degree)*sum;      
        return y 
    
    def destructiveManipu(self,degree):
        l=self.entry.tolist()              
        for index in range(0,10):
            random.seed(time.time())
            tem=0
            if(random.random()<self.poissonFunc(index,degree)):
                random.seed(time.time())                
                tem=random.randint(0,9)                                                                
                ori=l[index]
                l[index]=tem
                i=self.entry.tolist().index(ori)
                l[i]=ori   
        for index in range(0,10): 
            self.entry[index]=l[index];
        
    def constructiveManipu(self,degree):
        l=self.entry.tolist()              
        for index in range(0,10):
            random.seed(time.time())
            tem=0
            if(random.random()<self.poissonFunc(10-index,degree)):
                random.seed(time.time())                
                tem=random.randint(0,9)                                                                
                ori=l[index]
                l[index]=tem
                i=self.entry.tolist().index(ori)
                l[i]=ori   
        for index in range(0,10): 
            self.entry[index]=l[index];