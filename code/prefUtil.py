'''
Created on Mar 5, 2015

@author: Akshat
'''

class SushiPrefUtil(object):
    '''
    classdocs
    '''
    sushiPref = None

    def __init__(self, sPref):
        '''
        Constructor
        '''
        self.sushiPref = sPref
    
    def getCount(self, sushiName):
        df = self.sushiPref.getDf()
        
        count = df[sushiName].value_counts()
        count = count.sort_index()
        
        return count
        