'''
Created on Mar 5, 2015

@author: Akshat
'''
from code.sf.sf_stv import ImplSTV
from code.sf.sf_irv import ImplIRV
from code.sf.sf_plurality import ImplPlurality
from code.sf.sf_plurality_at_large import ImplPluralityAtLarge
from code.pref_matrix_plot import PrefPlotter
from MutationFunc.RandomSwap import Mutation

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'

def executeExp():

    pref_plotter = PrefPlotter('C:/Users/pengjie137/git/mutation-tolerance-voting/prefrences/sushi3_preflib/ED-00015-00000001.soc')
    pref_plotter.plotGraph()
    pref_plotter.print_matrix()
    
    pc = ImplSTV(pref_plotter.raw_pref)
    pc = ImplIRV(pref_plotter.raw_pref)
    pc = ImplPlurality(pref_plotter.raw_pref)
    pc = ImplPluralityAtLarge(pref_plotter.raw_pref)
    OutputFilePath="C:/Users/pengjie137/git/mutation-tolerance-voting/prefrences/NormalNoise"
#     pu = SushiPrefUtil(pr)
#     pref_matrix = pu.gen_pref_matrix() 
#      
#      
#     print(pref_matrix)
#      
#     # For Graph Plot
#     pref_matrix.plot()
#     plt.show()
    #print(pref_plotter.raw_pref.getDf())
    for num in range(1,11):
        df_copy = pref_plotter.raw_pref.getDf().copy(True)
        for index, row in df_copy.iterrows():
            randomswap=Mutation(row,0.5)
            randomswap.normalNoise();
#
# df_copy.to_csv('C:/Users/Akshat/git/mutation-tolerance-voting/output/o2.soc', encoding='utf-8', index=True)
# PrefPlotter('C:/Users/Akshat/git/mutation-tolerance-voting/output/o2.soc').plotGraph()
#     for index, row in pref_plotter.raw_pref.getDf().iterrows():
#         randomswap=Mutation(row,0.5)
#         randomswap.normalNoise()
#         print(row)
        df_copy.to_csv(OutputFilePath+str(num)+".csv", encoding='utf-8', index=True)
#         PrefPlotter(OutputFilePath+str(num)+".csv").plotGraph()
    
    OutputFilePath="C:/Users/pengjie137/git/mutation-tolerance-voting/prefrences/TotalMutation"
    for num in range(1,11):
        df_copy = pref_plotter.raw_pref.getDf().copy(True)
        for index, row in df_copy.iterrows():
            randomswap=Mutation(row,0.5)
            randomswap.randomSwap()
        df_copy.to_csv(OutputFilePath+str(num)+".csv", encoding='utf-8', index=True)
if __name__ == '__main__':
    executeExp()