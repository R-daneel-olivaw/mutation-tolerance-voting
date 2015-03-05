'''
Created on Mar 5, 2015

@author: Akshat
'''

import pandas as pd


class SushiReader(object):
    '''
    classdocs
    '''
    csv = None
    df = None
    
    def __init__(self, csvPath):
        '''
        Constructor
        '''
        self.csv = csvPath
  
    def loadUp(self):
        
        localdf = pd.read_csv(self.csv, skiprows=12, names=['#','ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'])
        del localdf['#']
        
        self.df = localdf
    
    def getDf(self):
        
        return self.df
    
        
        
