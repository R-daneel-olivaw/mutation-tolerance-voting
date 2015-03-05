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
    
    def getRankCount(self, rank):
        df = self.sushiPref.getDf()
        
        count = df[rank].value_counts()
        count = count.sort_index()
        
        return count
        