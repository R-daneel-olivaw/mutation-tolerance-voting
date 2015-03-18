'''
Created on Mar 17, 2015

@author: Akshat
'''
from code.pref_sf_conv import PrefSFConverter
from pyvotecore.plurality_at_large import PluralityAtLarge

class ImplPluralityAtLarge(object):
    '''
    classdocs
    '''
    
    def __init__(self, raw_pref):
        '''
        Constructor
        '''
        
        self.processed_pref = PrefSFConverter(raw_pref).convert_plurality_at_large()
        self.run_plurality_at_large()
    
    def run_plurality_at_large(self):
        
        output = PluralityAtLarge(self.processed_pref, required_winners=3).as_dict()
        print('##Plurality At Large Winners##')
        #print(output)
        print(output['winners'])
        print(output['tallies'])
        print('##Plurality At Large Winners##')
        print()