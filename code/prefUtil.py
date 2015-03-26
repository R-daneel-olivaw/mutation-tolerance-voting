'''
Created on Mar 5, 2015

@author: Akshat
'''
from pandas.core.frame import DataFrame

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
    
    def gen_pref_matrix(self):
        
        rank1 = self.getRankCount('01')
        rank2 = self.getRankCount('02')
        rank3 = self.getRankCount('03')
        rank4 = self.getRankCount('04')
        rank5 = self.getRankCount('05')
        rank6 = self.getRankCount('06')
        rank7 = self.getRankCount('07')
        rank8 = self.getRankCount('08')
        rank9 = self.getRankCount('09')
        rank10 = self.getRankCount('10')
        
        fullPref = DataFrame(dict(r1=rank1, r2=rank2, r3=rank3, r4=rank4, r5=rank5, r6=rank6, r7=rank7, r8=rank8, r9=rank9, r10=rank10))
        fullPref.index.name = 'SushiName'
        
        fullPref = fullPref.transpose()
        
        '''
        Big work arroud in the below line the ordering should have been,
        ['ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki']
        but this was not working as the column r10 was being wrongly placed after r1
        '''
        fullPref.columns = ['ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki']
        
        fullPref['indexNumber'] = [int(i[1:]) for i in fullPref.index]
        fullPref = fullPref.sort(['indexNumber'], ascending=[True])
        fullPref = fullPref.drop('indexNumber', 1)
        
        return fullPref
        