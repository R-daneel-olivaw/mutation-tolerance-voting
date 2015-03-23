'''
Created on Mar 13, 2015

@author: Akshat
'''
import pandas as pd
import matplotlib.pyplot as plt
from code.prefreaders import SushiPref
from code.prefUtil import SushiPrefUtil

class PrefPlotter(object):
    '''
    classdocs
    '''

    def load_pref(self):

        self.raw_pref = SushiPref( self.pref_path)
        self.raw_pref.loadUp()
    
        self.pref_util = SushiPrefUtil(self.raw_pref)
        self.pref_matrix = self.pref_util.gen_pref_matrix() 
        
    
    def load_pref_o(self):

        self.raw_pref = SushiPref( self.pref_path)
        self.raw_pref.loadUp_2()
    
        self.pref_util = SushiPrefUtil(self.raw_pref)
        self.pref_matrix = self.pref_util.gen_pref_matrix() 
    
    
    def __init__(self, pref_path, is_noisy=False):
        '''
        Constructor
        '''
        if is_noisy:
            self.pref_path = pref_path
            self.load_pref_o()
        else:
            self.pref_path = pref_path
            self.load_pref()
        
    
    def print_matrix(self):
        print(self.pref_matrix) 
        
    def plotGraph(self):
        
        # Set some Pandas options
        pd.set_option('display.notebook_repr_html', False)
        pd.set_option('display.max_columns', 20)
        pd.set_option('display.max_rows', 25)
        
            # For Graph Plot
        self.pref_matrix.plot()
        plt.show()
