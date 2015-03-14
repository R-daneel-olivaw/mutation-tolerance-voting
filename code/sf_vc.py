'''
Created on Mar 13, 2015

@author: Akshat
'''
from pyvotecore.schulze_method import SchulzeMethod
from pyvotecore.stv import STV

class PrefCounter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
#         ballots = [
#                    { "count":3, "ballot":[["A"], ["C"], ["D"], ["B"]] },
#                    { "count":9, "ballot":[["B"], ["A"], ["C"], ["D"]] },
#                    { "count":8, "ballot":[["C"], ["D"], ["A"], ["B"]] },
#                    { "count":5, "ballot":[["D"], ["A"], ["B"], ["C"]] },
#                    { "count":5, "ballot":[["D"], ["B"], ["C"], ["A"]] }
#                 ]
#         print(SchulzeMethod(ballots, ballot_notation=0).as_dict())
        
                # Generate data
        input_pr = [
            {"count": 56, "ballot": ["c1", "c2", "c3", "c4"]},
            {"count": 40, "ballot": ["c4", "c2", "c3", "c1"]},
            {"count": 20, "ballot": ["c3", "c4", "c1", "c2"]},
            {"count": 20, "ballot": ["c3", "c1", "c4", "c2"]}
        ]
        output = STV(input_pr, required_winners=2).as_dict()
        print(output)
        
        print('END')
