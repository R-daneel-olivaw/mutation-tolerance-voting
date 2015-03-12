'''
Created on Mar 5, 2015

@author: Akshat
'''
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'

def executeExp():
    # Set some Pandas options
    pd.set_option('display.notebook_repr_html', False)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 25)
    
    pr = SushiPref('D:\Lectures\Winter2015\CS886\Project\sushi3_preflib\sushi3_preflib\ED-00015-00000001.soc')
    pr.loadUp()

    pu = SushiPrefUtil(pr)
    pref_matrix = pu.gen_pref_matrix() 
    
    
    print(pref_matrix)
    
    # For Graph Plot
    pref_matrix.plot()
    plt.show()

if __name__ == '__main__':
    from code.prefreaders import SushiPref
    from code.prefUtil import SushiPrefUtil
    executeExp()
