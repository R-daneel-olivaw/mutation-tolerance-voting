'''
Created on Mar 23, 2015

@author: Akshat
'''
import pickle

class ResultAggregator(object):
    '''
    classdocs
    '''


    def __init__(self, output_directry, file_name):
        '''
        Constructor
        '''
        self.output_directry = output_directry
        self.file_name = file_name
        
    def pickle_results(self, stv_result, irv_result, plurality_result, plurality_large_result):
        
        output = {}
        
        output['STV'] = stv_result
        output['IRV'] = irv_result
        output['PLURALITY'] = plurality_result
        output['PLURALITY_AT_LARGE'] = plurality_large_result

        path = None
          
        path = self.output_directry + '/' + self.file_name
            
        pickle.dump(output, open(path, "wb"))
        
        return path
    
    def read_pickle_sample(self, pickle_directory, pickle_name):
        
        results = pickle.load(open(pickle_directory + '/' + pickle_name, "rb"))
        
        return results
        
