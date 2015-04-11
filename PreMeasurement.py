'''
Created on Mar 25, 2015

@author: PengPeng
'''

from code.result_agg import ResultAggregator
import scipy.stats as stats
import pickle

class ResultMeasurement(object):
    '''
    classdocs
    '''
    
    def read_pickle_path(self, pickle_path):
        
        results = pickle.load(open(pickle_path, "rb"))
        
        return results


    def __init__(self, NoisePicklePath, NoNoisePicklePath):
        '''
        Constructor
        '''
        self.NoisePicklePath = NoisePicklePath
        self.NoNoisePicklePath = NoNoisePicklePath
        
        self.noisePickleInstance = self.read_pickle_path(self.NoisePicklePath)
        self.noNoisePickleInstance = self.read_pickle_path(self.NoNoisePicklePath)
         
#         print(self.noisePickleInstance["PLURALITY_AT_LARGE"]["winners"])
    
    def CalculateRankingForSTV(self):
        lstRounds = self.noisePickleInstance["STV"]["rounds"]
        lstLastRound = lstRounds[7]["winners"]
        
#         return list(lstLastRound)[]
        lstRanking = []
        lstRanking.append(list(lstRounds[0]["winners"])[0])
        lstRanking.append(list(lstLastRound)[0])
        lstRanking.append(list(lstLastRound)[1])
        
        
        for key in lstRounds[7]["tallies"].keys():
            if(key != list(lstLastRound)[0] and key != list(lstLastRound)[1]):
                loserInLastRound = key
        
        lstRanking.append(loserInLastRound)

        for i in range(6, 0, -1):
            lstRanking.append(lstRounds[i]["loser"])

        return lstRanking
#         return self.noisePickleInstance["STV"]["rounds"]
    
    def CalculateRankingForIRV(self):
        
        lstRounds = self.noisePickleInstance["IRV"]["rounds"]
        lstRanking = []
        
#         lstRanking.append(self.noisePickleInstance["IRV"]["winner"])
        lstLastRoundValue = []
        for i in lstRounds[7]["tallies"].values():
            lstLastRoundValue.append(i)
        
        lstLastRoundValue.sort(reverse = True)
        
        for i in range(0, 3):
            for key, value in lstRounds[7]["tallies"].items():
                if(lstLastRoundValue[i] == value):
                    lstRanking.append(key)
                    
        for i in range(6, -1, -1):
            lstRanking.append(lstRounds[i]["loser"])
            
        return lstRanking
    
    def CalculateRankingForPlurality(self):
        lstRanking = []
        lstTallyValues = []
        
        for i in self.noisePickleInstance["PLURALITY"]["tallies"].values():
            lstTallyValues.append(i)
            
        lstTallyValues.sort(reverse=True)

        for i in range(0, 10):
            for key, value in self.noisePickleInstance["PLURALITY"]["tallies"].items():
                if(lstTallyValues[i] == value):
                    lstRanking.append(key)
                    
        return lstRanking
    
    def CalculateRankingForPluralityAtLarge(self):
        lstRanking = []
        lstTallyValues = []
        
        for i in self.noisePickleInstance["PLURALITY_AT_LARGE"]["tallies"].values():
            lstTallyValues.append(i)
            
        lstTallyValues.sort(reverse=True)

        for i in range(0, 10):
            for key, value in self.noisePickleInstance["PLURALITY_AT_LARGE"]["tallies"].items():
                if(lstTallyValues[i] == value):
                    lstRanking.append(key)        
        return lstRanking

        
    def CalculatektDistance(self, originalRanking, MutatedRanking):
        
        return stats.kendalltau(originalRanking, MutatedRanking)
    
    def MeasureMultipleWinner(self):
        
        lstWinnersNoise = list(self.noisePickleInstance)
        lstWinnersNoNoise = list(self.noNoisePickleInstance["STV"]["winners"])
        
        
#         for i in self.noisePickleInstance["IRV"]["rounds"]:
#             print(i)
#         print(self.noisePickleInstance["IRV"])
#         return len(self.noisePickleInstance["IRV"]["rounds"])
#        return self.noisePickleInstance["STV"]
#         return lstWinnersNoise
        #calculate the kendalltauDistance of two rankings
#        ktDistance = stats.kendalltau(lstWinnersNoise, lstWinnersNoNoise)
        
        return self.noisePickleInstance["PLURALITY_AT_LARGE"]
