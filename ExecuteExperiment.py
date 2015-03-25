'''
Created on Mar 5, 2015

@author: Akshat
'''
from MutationFunc.RandomSwap import Mutation
import PrefMutationRandom
from code.pref_matrix_plot import PrefPlotter
from code.sf.sf_irv import ImplIRV
from code.sf.sf_plurality import ImplPlurality
from code.sf.sf_plurality_at_large import ImplPluralityAtLarge
from code.sf.sf_stv import ImplSTV
from code.result_agg import ResultAggregator

output_directry = 'C:/Users/Akshat/git/mutation-tolerance-voting/output'

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'
def executeExp():

    pref_plotter = PrefPlotter('C:/Users/Akshat/git/mutation-tolerance-voting/prefrences/sushi3_preflib/ED-00015-00000001.soc')
    # pref_plotter.plotGraph()
    # pref_plotter.print_matrix()
    
    
    stv_result = ImplSTV(pref_plotter.raw_pref,).run_stv()    
    irv_result = ImplIRV(pref_plotter.raw_pref).run_irv()
    plurality_result = ImplPlurality(pref_plotter.raw_pref).run_plurality()
    plurality_large_result = ImplPluralityAtLarge(pref_plotter.raw_pref).run_plurality_at_large()
    
    r_agg = ResultAggregator(output_directry, 'no-noise.pik')
    r_agg.pickle_results(stv_result, irv_result, plurality_result, plurality_large_result)
    
    # READ PICKLE SAMPLE
    read_pickle_sample = r_agg.read_pickle_sample(output_directry, 'no-noise.pik')
    print(read_pickle_sample)
    # READ PICKLE SAMPLE
    
    p8peng_out = PrefMutationRandom.MutationRandom('C:/Users/Akshat/git/mutation-tolerance-voting/prefrences/sushi3_preflib/ED-00015-00000001.soc').GetResult(0.01, 0, 'C:/Users/Akshat/git/mutation-tolerance-voting/output')
    PrefPlotter(p8peng_out, True).plotGraph()
     
    # print(pref_plotter.raw_pref.getDf())
    
#     df_copy = pref_plotter.raw_pref.getDf().copy(True)
#     for index, row in df_copy.iterrows():
#         randomswap=Mutation(row,0.5)
#         randomswap.randomSwap()
#         #print(row)
#            
#     df_copy.to_csv('C:/Users/Akshat/git/mutation-tolerance-voting/output/o2.soc', encoding='utf-8', index=True) 
#     PrefPlotter('C:/Users/Akshat/git/mutation-tolerance-voting/output/o2.soc').plotGraph()    
    
if __name__ == '__main__':
    executeExp()

