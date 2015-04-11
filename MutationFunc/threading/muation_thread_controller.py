'''
Created on Mar 25, 2015

@author: Akshat
'''
import ntpath
import PrefMutationRandom
from code.pref_matrix_plot import PrefPlotter
from code.sf.sf_irv import ImplIRV
from code.sf.sf_plurality import ImplPlurality
from code.sf.sf_plurality_at_large import ImplPluralityAtLarge
from code.sf.sf_stv import ImplSTV
from code.result_agg import ResultAggregator
from threading import Thread
import threading
from MutationFunc.RandomSwap import Mutation
from PreMeasurement import ResultMeasurement

class MuationThreadController(object):
    '''
    classdocs
    '''

    
    def compare_ranking(self, no_noise_pickle_path, noisy_pickle_path):
        rm = ResultMeasurement(noisy_pickle_path, no_noise_pickle_path)
        
        distance_stv = rm.CalculatektDistance(originalRanking, rm.CalculateRankingForSTV())
    
    def fork_mutate_index_extreme_degree(self, degree):
        
        path = None            
        path = self.output_directry 
        
        p8peng_out = PrefMutationRandom.MutationRandom(self.pref_path).GetResult(degree, 0, path)
        noisyPP = PrefPlotter(p8peng_out, True)    
        noisy_pickle_path = self.compute_noisy_results(noisyPP, self.path_leaf(p8peng_out))
        
        self.compare_ranking(self.no_noise_pickle_path, noisy_pickle_path)
        # threading.current_thread().noisy_pickle_path = noisy_pickle_path
        
        print('Completed ', degree)
    
    def compute_noisy_results(self, noisyPP, pickle_name):
    
        stv_result = ImplSTV(noisyPP.raw_pref,).run_stv()    
        irv_result = ImplIRV(noisyPP.raw_pref).run_irv()
        plurality_result = ImplPlurality(noisyPP.raw_pref).run_plurality()
        plurality_large_result = ImplPluralityAtLarge(noisyPP.raw_pref).run_plurality_at_large()
        
        r_agg = ResultAggregator(self.output_directry, pickle_name + str(self.index) + '.pik')
        noisy_pickle_path = r_agg.pickle_results(stv_result, irv_result, plurality_result, plurality_large_result)
        
        return noisy_pickle_path
        
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def __init__(self, config, pref_path, output_directry, no_noise_pickle_path, index=None):
        '''
        Constructor
        '''
        self.config = config
        self.pref_path = pref_path
        self.output_directry = output_directry
        self.no_noise_pickle_path = no_noise_pickle_path
        self.index = index
        

    def get_config_value(self, config_key):
        value = self.config[config_key]
        return value
    
    
    def fork_mutate_index_extreme(self, worker_list):
        
        degree_list = self.get_config_value('extremes_noise_level_list')
        degree_list = map(float, degree_list.split(','))
        
        for degree in degree_list:
            print('WORKING ON ', degree)
            worker = Thread(target=self.fork_mutate_index_extreme_degree, args=(degree,))
            # worker.setDaemon(True)
            worker.start()
            
            worker_list.append(worker)
            
    def fork_mutate_total_degree(self, degree):
        
        print('WORKING ON TOTAL degree :', degree)
        
        randomswap = Mutation(degree, self.pref_path, self.output_directry)
        o_path = randomswap.mutate_total()
        
        print(o_path)
        
        noisyPP = PrefPlotter(o_path, True)    
        self.compute_noisy_results(noisyPP, self.path_leaf(o_path))
        
        print('Completed total degree :', degree)
    
    def fork_mutate_total(self, worker_list, degree_list):
        
        for degree in degree_list:
        
            worker = Thread(target=self.fork_mutate_total_degree, args=(degree,))
            
            worker.start()
            
            worker_list.append(worker)
