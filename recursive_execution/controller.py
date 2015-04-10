'''
Created on Apr 10, 2015

@author: Akshat
'''
from multiprocessing import Pool, Queue, Manager
from time import sleep
import ExecuteExperiment

class RecursiveExecutionController(object):
    '''
    classdocs
    '''
    
    def __init__(self, execution_repetition_count, execution_parallel_process_count, execution_output_filepath):
        '''
        Constructor
        '''
        self.execution_repetition_count = execution_repetition_count
        self.execution_parallel_process_count = execution_parallel_process_count
        self.execution_output_filepath = execution_output_filepath
        
    def execute_single_experiment(self, args):
        
        index, q = args
        
        print('Hi Akshat - ', index)
        
        ExecuteExperiment.executeExp(index)
        
        q.put(('process-', index, ' checking-in'))
        
    def start(self):
        
        index = range(0, self.execution_repetition_count)
        print('Creating pool with %d processes\n' % self.execution_parallel_process_count)
        
        m = Manager()
        q = m.Queue()
        res = None
        with Pool(processes=self.execution_parallel_process_count) as pool:
            
            print('starting')
            args = ((i, q) for i in index)
            res = pool.map_async(func=self.execute_single_experiment, iterable=args, chunksize=1)
            res.get()
            
        for i in range(len(index)):
            print('\t', q.get())
            
            
    
