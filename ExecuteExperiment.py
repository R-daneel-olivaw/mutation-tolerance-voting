'''
Created on Mar 5, 2015

@author: Akshat
'''
from MutationFunc.RandomSwap import Mutation
from code.pref_matrix_plot import PrefPlotter
from code.sf.sf_irv import ImplIRV
from code.sf.sf_plurality import ImplPlurality
from code.sf.sf_plurality_at_large import ImplPluralityAtLarge
from code.sf.sf_stv import ImplSTV
from code.result_agg import ResultAggregator
from MutationFunc.threading.muation_thread_controller import MuationThreadController
import ntpath
import configparser

output_directry = None
input_file_path = None
mutate_index_extreme = [0.1]
ini_path = 'experiment_config.ini'

def parse_config(ini_path):
    
    config = configparser.ConfigParser()
    config.sections()
    config.read(ini_path)
    
    experiment_config = config['sf']
    
    global output_directry
    output_directry = experiment_config['output_directry']
    
    global input_file_path
    input_file_path = experiment_config['input_file_path']

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def compute_noisy_results(noisyPP, pickle_name):
    
    stv_result = ImplSTV(noisyPP.raw_pref,).run_stv() 
    irv_result = ImplIRV(noisyPP.raw_pref).run_irv()
    plurality_result = ImplPlurality(noisyPP.raw_pref).run_plurality()
    plurality_large_result = ImplPluralityAtLarge(noisyPP.raw_pref).run_plurality_at_large()
    
    r_agg = ResultAggregator(output_directry, pickle_name + '.pik')
    r_agg.pickle_results(stv_result, irv_result, plurality_result, plurality_large_result)


def compute_no_noise_results(pref_plotter):
    
    stv_result = ImplSTV(pref_plotter.raw_pref,).run_stv()    
    irv_result = ImplIRV(pref_plotter.raw_pref).run_irv()
    plurality_result = ImplPlurality(pref_plotter.raw_pref).run_plurality()
    plurality_large_result = ImplPluralityAtLarge(pref_plotter.raw_pref).run_plurality_at_large()
    
    r_agg = ResultAggregator(output_directry, 'no-noise.pik')
    r_agg.pickle_results(stv_result, irv_result, plurality_result, plurality_large_result)
    
    # READ PICKLE SAMPLE
    read_pickle_sample = r_agg.read_pickle_sample(output_directry, 'no-noise.pik')
    print(read_pickle_sample)
    
    print(read_pickle_sample['STV']['winners'])
    
    temp_a = []
    for i in read_pickle_sample['STV']['winners']:
        temp_a.append(i)
        
    print(temp_a[0])
    # READ PICKLE SAMPLE


def get_config_key(ini_key):
    config = configparser.ConfigParser()
    config.sections()
    config.read(ini_path)
    
    experiment_config = config[ini_key]
    
    return experiment_config


# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'
def executeExp():
    
    parse_config(ini_path)
    print('output_directry - ', output_directry)
    print('input_file_path - ', input_file_path)
    
    pref_plotter = PrefPlotter(input_file_path)
    # pref_plotter.plotGraph()
    # pref_plotter.print_matrix()
    
    compute_no_noise_results(pref_plotter)
    
    worker_list = []
    
    noise_config = get_config_key('noise')
    m_controller = MuationThreadController(noise_config, input_file_path, output_directry)
    
    m_controller.fork_mutate_index_extreme(worker_list)
    # m_controller.fork_mutate_total(worker_list, [0.5])
    
    for worker in worker_list:
        worker.join() 
    
    print('**********DONE**********')
     
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
