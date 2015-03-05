'''
Created on Mar 5, 2015

@author: Akshat
'''
# names=['#','ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki']

import pandas as pd


class SushiPref(object):
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
        
        localdf = pd.read_csv(self.csv, skiprows=12, names=['#', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10'])
        
        del localdf['#']
        
        self.df = localdf
    
    def getDf(self):
        
        return self.df
    
        
        
