'''
Created on Mar 23, 2015

@author: pengjie137
'''
import random
from datetime import datetime
import time
import math

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
    
    def randomSwap(self):
        random.seed(datetime.now())
        if(random.random()<self.degree):
            random.shuffle(self.entry)
    
    def normalNoise(self):
        for index in range(1,10):
            random.seed(time.time())
            if(random.random()<self.gaussianFunc(index)):
                random.seed(time.time())
                self.entry[index]=random.randint(0,9)
        list.sort(self.entry.tolist(),key=lambda k: self.entry[k]);
        
    
    def gaussianFunc(self,index):
        x=(index-5.5)*4/9
        y=math.exp(-x*x/2)/math.sqrt(2*math.pi)
        return y   