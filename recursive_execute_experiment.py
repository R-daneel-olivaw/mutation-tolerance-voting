'''
Created on Apr 10, 2015

@author: Akshat
'''
import configparser
from recursive_execution.controller import RecursiveExecutionController

ini_path = 'experiment_config.ini'
execution_repetition_count = None
execution_parallel_process_count = None
execution_output_filepath = None

def get_config_key(ini_key, ini_path):
    config = configparser.ConfigParser()
    config.sections()
    config.read(ini_path)
    
    experiment_config = config[ini_key]
    
    return experiment_config

def parse_config(ini_path):
    
    experiment_config = get_config_key('experiment_execution', ini_path)
    
    global execution_repetition_count
    execution_repetition_count = int(experiment_config['execution_repetition_count'])
    
    global execution_parallel_process_count
    execution_parallel_process_count = int(experiment_config['execution_parallel_process_count'])
    
    global execution_output_filepath 
    execution_output_filepath = experiment_config['execution_output_filepath']


def execute_experiment():
    parse_config(ini_path)
    
    print('execution_repetition_count -> ', execution_repetition_count)
    print('execution_parallel_process_count -> ', execution_parallel_process_count)
    print('execution_output_filepath -> ', execution_output_filepath)
    
    rec = RecursiveExecutionController(execution_repetition_count, execution_parallel_process_count, execution_output_filepath)
    rec.start()


if __name__ == '__main__':
    execute_experiment()
