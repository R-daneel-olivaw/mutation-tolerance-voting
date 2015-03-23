'''
Created on Mar 15, 2015

@author: Akshat
'''
from code.pref_sf_conv import PrefSFConverter
from pyvotecore.plurality import Plurality

class ImplPlurality(object):
    '''
    classdocs
    '''


    def __init__(self, raw_pref):
        '''
        Constructor
        '''
        
        self.processed_pref = PrefSFConverter(raw_pref).convert_single_vote()
        self.run_plurality_at_large()
    
    def run_plurality_at_large(self):
        
        output = Plurality(self.processed_pref).as_dict()
        print('##Plurality Winners##')
        #print(output)
        print(output['winner'])
        print(output['tallies'])
        print('##Plurality Winners##')
        print()
        