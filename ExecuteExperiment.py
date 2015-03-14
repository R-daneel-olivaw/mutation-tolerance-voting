'''
Created on Mar 5, 2015

@author: Akshat
'''
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from code.sf_vc import PrefCounter
from code.pref_matrix_plot import PrefPlotter

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'

def executeExp():

    pref_plotter = PrefPlotter('D:\Lectures\Winter2015\CS886\Project\sushi3_preflib\sushi3_preflib\ED-00015-00000001.soc')
    pref_plotter.plotGraph()
    
    pc = PrefCounter()

if __name__ == '__main__':
    from code.prefreaders import SushiPref
    from code.prefUtil import SushiPrefUtil
    executeExp()
