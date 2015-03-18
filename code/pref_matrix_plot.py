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

        self.raw_pref = SushiPref('D:\Lectures\Winter2015\CS886\Project\sushi3_preflib\sushi3_preflib\ED-00015-00000001.soc')
        self.raw_pref.loadUp()
    
        self.pref_util = SushiPrefUtil(self.raw_pref)
        self.pref_matrix = self.pref_util.gen_pref_matrix() 
    
    
    def __init__(self, pref_path):
        '''
        Constructor
        '''
        self.pref_path = pref_path
        self.load_pref()
        
        
    def plotGraph(self):
        
        # Set some Pandas options
        pd.set_option('display.notebook_repr_html', False)
        pd.set_option('display.max_columns', 20)
        pd.set_option('display.max_rows', 25)
        
            # For Graph Plot
        self.pref_matrix.plot()
        plt.show()
