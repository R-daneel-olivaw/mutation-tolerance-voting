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

# bNoise is a boolean value for deciding to calculate original ranking or mutated ranking; 
# 0 means calculating mutated one, else calculate original one
    def CalculateRankingForSTV(self, bNoise):
        
        if(bNoise == 0):
            lstRounds = self.noisePickleInstance["STV"]["rounds"]
            lstLastRound = lstRounds[7]["winners"]
        
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
        
        else:
            lstRounds = self.noNoisePickleInstance["STV"]["rounds"]
            lstLastRound = lstRounds[7]["winners"]
        
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
                    
    
    def CalculateRankingForIRV(self, bNoise):
        
        if(bNoise == 0):
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
        
        else:
            lstRounds = self.noNoisePickleInstance["IRV"]["rounds"]
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
    
    def CalculateRankingForPlurality(self, bNoise):
        
        if(bNoise == 0):
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
    
        else:
            lstRanking = []
            lstTallyValues = []
            
            for i in self.noNoisePickleInstance["PLURALITY"]["tallies"].values():
                lstTallyValues.append(i)
                
            lstTallyValues.sort(reverse=True)
    
            for i in range(0, 10):
                for key, value in self.noNoisePickleInstance["PLURALITY"]["tallies"].items():
                    if(lstTallyValues[i] == value):
                        lstRanking.append(key)
                        
            return lstRanking            
        
    def CalculateRankingForPluralityAtLarge(self, bNoise):
        
        if(bNoise == 0):
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
        
        else:
            lstRanking = []
            lstTallyValues = []
            
            for i in self.noNoisePickleInstance["PLURALITY_AT_LARGE"]["tallies"].values():
                lstTallyValues.append(i)
                
            lstTallyValues.sort(reverse=True)
    
            for i in range(0, 10):
                for key, value in self.noNoisePickleInstance["PLURALITY_AT_LARGE"]["tallies"].items():
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
