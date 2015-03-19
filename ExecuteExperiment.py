'''
Created on Mar 5, 2015

@author: Akshat
'''
from code.sf.sf_stv import ImplSTV
from code.sf.sf_irv import ImplIRV
from code.sf.sf_plurality import ImplPlurality
from code.sf.sf_plurality_at_large import ImplPluralityAtLarge
from code.pref_matrix_plot import PrefPlotter

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'

def executeExp():

    pref_plotter = PrefPlotter('C:/Users/pengjie137/git/mutation-tolerance-voting/prefrences/sushi3_preflib/ED-00015-00000001.soc')
    #pref_plotter.plotGraph()
    pref_plotter.print_matrix()
    
    pc = ImplSTV(pref_plotter.raw_pref)
    pc = ImplIRV(pref_plotter.raw_pref)
    pc = ImplPlurality(pref_plotter.raw_pref)
    pc = ImplPluralityAtLarge(pref_plotter.raw_pref)

if __name__ == '__main__':
    executeExp()