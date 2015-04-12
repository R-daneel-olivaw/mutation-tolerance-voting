'''
Created on Apr 12, 2015

@author: Akshat
'''
import pandas as pd
import matplotlib.pyplot as plt

class ResultCollator(object):
    '''
    classdocs
    '''
    
    distance_df = None

    def __init__(self, worker_list, output_directory):
        '''
        Constructor
        '''
        self.output_directory = output_directory
        self.worker_list = worker_list
        
    def collate(self):
        rows = []
        for worker in self.worker_list:
#             dist_stv = worker.distance_stv
            dist_irv = worker.distance_irv
            
            row={}
#             row['stv_dist'] = dist_stv[0]
#             row['stv_pval'] = dist_stv[1]
            
            row['irv_dist'] = dist_irv[0]
            row['irv_pval'] = dist_irv[1]            
            rows.append(row)
            
        df = pd.DataFrame(rows)
        self.distance_df = df
        
        ocsv_path = self.output_directory+'/result_distance.csv' 
        df.to_csv(ocsv_path, encoding='utf-8', index=True)
    
    def graph_results(self):
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
    
        # ax.set_xlim([0,10])
        # ax.set_ylim([0,10])
        
        ax.set_title('All Percentiles')
        ax.set_xlabel("index")
        ax.set_ylabel("Price($)")
        
        ax.scatter(self.distance_df.index.values, self.distance_df['stv'], edgecolors='none', s=5, color='red', label='50 percentile', alpha=0.5)
#         ax.scatter(df.index.values, df['75 percentile'], edgecolors='none', s=5, color='blue', label='75 percentile', alpha=0.5)
#         ax.scatter(df.index.values, df['90 percentile'], edgecolors='none', s=5, color='yellow', label='90 percentile', alpha=0.5)
#         ax.scatter(df.index.values, df['95 percentile'], edgecolors='none', s=5, color='green', label='95 percentile', alpha=0.5)
#         ax.scatter(df.index.values, df['100 percentile'], edgecolors='none', s=5, color='magenta', label='100 percentile', alpha=0.5)
        
        ax.set_ylim(80)
        ax.set_xlim(0)
        ax.legend(loc=0, scatterpoints=1)
        # ax.scatter(scipy.randn(100), scipy.randn(100), c='r')
        
        fig.set_size_inches(15, 5)
        fig.savefig(self.output_directory + 'distance' + '_ALL.png', bbox_inches='tight')
