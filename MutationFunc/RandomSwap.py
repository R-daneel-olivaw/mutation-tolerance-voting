'''
Created on Mar 23, 2015

@author: pengjie137
'''
import random
from datetime import datetime
import time
import math
from code.prefreaders import SushiPref
from code.prefUtil import SushiPrefUtil
from code.pref_matrix_plot import PrefPlotter

class Mutation(object):
    '''
    classdocs
    '''

    entry = None
    degree = 0.5
    def __init__(self, degree, pref_path, output_directory):
        '''
        Constructor
        '''
        self.degree = degree
        self.pref_path = pref_path
        self.output_directory = output_directory
        self.pref_plotter = PrefPlotter(pref_path)
        
    def LoadPref(self):
        
        self.raw_pref = SushiPref(self.prefpath)
        self.raw_pref.loadUp()
    
    def randomSwap(self, entry):
        random.seed(datetime.now())
        if(random.random() < self.degree):
            random.shuffle(entry)
    
    def normalNoise(self, entry):
        for index in range(1, 10):
            random.seed(time.time())
            if(random.random() < self.gaussianFunc(index)):
                random.seed(time.time())
                entry[index] = random.randint(0, 9)
        list.sort(entry.tolist(), key=lambda k: entry[k]);
        
    
    def gaussianFunc(self, index):
        x = (index - 5.5) * 4 / 9
        y = math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
        return y   
    
    def mutate_total(self):
        
        df_copy = self.pref_plotter.raw_pref.getDf()
        for index, row in df_copy.iterrows():
            self.normalNoise(row);
        
        t_path = self.output_directory + '/total' + str(self.degree) + ".csv"
        df_copy.to_csv(t_path, encoding='utf-8', index=True)
        
        return t_path
        
