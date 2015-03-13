'''
Created on Mar 13, 2015

@author: Akshat
'''
from pyvotecore.schulze_method import SchulzeMethod

class PrefCounter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ballots = [
                   { "count":3, "ballot":[["A"], ["C"], ["D"], ["B"]] },
                   { "count":9, "ballot":[["B"], ["A"], ["C"], ["D"]] },
                   { "count":8, "ballot":[["C"], ["D"], ["A"], ["B"]] },
                   { "count":5, "ballot":[["D"], ["A"], ["B"], ["C"]] },
                   { "count":5, "ballot":[["D"], ["B"], ["C"], ["A"]] }
                ]
        print(SchulzeMethod(ballots, ballot_notation = 0).as_dict())
        
        print('END')