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
    
    rank1 = pu.getRankCount('01')
    rank2 = pu.getRankCount('02')
    rank3 = pu.getRankCount('03')
    rank4 = pu.getRankCount('04')
    rank5 = pu.getRankCount('05')
    rank6 = pu.getRankCount('06')
    rank7 = pu.getRankCount('07')
    rank8 = pu.getRankCount('08')
    rank9 = pu.getRankCount('09')
    rank10 = pu.getRankCount('10')
    
    fullPref = DataFrame(dict(r1=rank1, r2=rank2, r3=rank3, r4=rank4, r5=rank5, r6=rank6, r7=rank7, r8=rank8, r9=rank9, r10=rank10))
    fullPref.index.name = 'SushiName'
    
    print('RESULTS...')
    
    fullPref = fullPref.transpose()
    fullPref.columns = ['ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki']
    print(fullPref)
    
    
    # For Graph Plot
    fullPref.plot()
    plt.show()
    

if __name__ == '__main__':
    from code.prefreaders import SushiPref
    from code.prefUtil import SushiPrefUtil
    executeExp()
