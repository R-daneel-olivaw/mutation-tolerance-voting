'''
Created on Mar 13, 2015

@author: Akshat
'''

class PrefSFConverter(object):
    '''
    classdocs
    '''


    def __init__(self, raw_pref):
        '''
        Constructor
        '''
        self.raw_pref = raw_pref
    
    def convert(self):
        df = self.raw_pref.getDf()
        
        df = df.replace([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], ['ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki']) 
        
        #print(df)
        
        df['concatenated'] = df['01'] + ',' + df['02'] + ',' + df['03'] + ',' + df['04'] + ',' + df['05'] + ',' + df['06'] + ',' + df['07'] + ',' + df['08'] + ',' + df['09'] + ',' + df['10']
        uq_pref = df['concatenated'].value_counts()
        
        input_pr = []
        for index, value in uq_pref.iteritems():
            #print(index,value)
            
            i_p = {}
            
            i_pref = index.split(",")
            i_count = value
            
            i_p['count'] = i_count
            i_p['ballot'] = i_pref
            
            input_pr.append(i_p)
            
        #print(input_pr)
        
        return input_pr
            
        
        
        
