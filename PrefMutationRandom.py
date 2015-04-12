'''
Created on Mar 18, 2015

@author: PengPeng
'''

from code.prefreaders import SushiPref
from code.prefUtil import SushiPrefUtil
from Crypto.Random.random import sample
import random

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'

class MutationRandom(object):
    '''
    classdocs
    '''
    
    def __init__(self, prefpath, index):
        '''
        Constructor
        '''
        
        self.prefpath = prefpath
        self.LoadPref()
        self.index = index
        
    def LoadPref(self):
        
        self.raw_pref = SushiPref(self.prefpath)
        self.raw_pref.loadUp()
                
    def GenerateRandom(self, Percentage, MutateType, OutputFilePath):
        numRow = len(self.raw_pref.getDf().index)               #get row count
        numRowMutate = round(numRow * Percentage)               #get mutated raw count
        lstRandomRaw = sample(range(0, numRow), numRowMutate)   #generate numRowMutate random numbers in range
        
        #Mutate votes on extremes when MutateType == 0 else muate votes in the middle
        #Extremes means the first two and the last two
        #votes in the middle means the rest six
        
#        print(lstRandomRaw)
        
        lstMutateIndexExtreme = [0, 1, 8, 9]
        lstMutateIndexMid = [2, 3, 4, 5, 6, 7]
        lstMutate = []
        
        if MutateType == 0:
            for iRow in range(0, len(lstRandomRaw)):
#                 print(self.raw_pref.getDf().iloc[lstRandomRaw[iRow]])
                for iElement in range(0, 4):
                    lstMutate.append(self.raw_pref.getDf().iloc[lstRandomRaw[iRow], lstMutateIndexExtreme[iElement]])
#                 print(lstMutate)
                lstMutated = sorted(lstMutate, key = lambda k: random.random())
#                print(lstMutated)
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 0] = lstMutated[0];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 1] = lstMutated[1];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 8] = lstMutated[2];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 9] = lstMutated[3];
#                print(self.raw_pref.getDf().iloc[lstRandomRaw[iRow]])
                
                del lstMutate[:]
                
#            self.raw_pref.getDf().to_csv(OutputFilePath, encoding='utf-8', index=True)                
            self.WriteToDirectory(OutputFilePath, Percentage, MutateType)    
                
        else:
            for iRow in range(0, len(lstRandomRaw)):
#                 print(self.raw_pref.getDf().iloc[lstRandomRaw[iRow]])
                for iElement in range(0, 6):
                    lstMutate.append(self.raw_pref.getDf().iloc[lstRandomRaw[iRow], lstMutateIndexMid[iElement]])
#                print(lstMutate)
                lstMutated = sorted(lstMutate, key = lambda k: random.random())
#                print(lstMutated)
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 2] = lstMutated[0];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 3] = lstMutated[1];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 4] = lstMutated[2];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 5] = lstMutated[3];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 6] = lstMutated[4];
                self.raw_pref.getDf().iloc[lstRandomRaw[iRow], 7] = lstMutated[5];
#                print(self.raw_pref.getDf().iloc[lstRandomRaw[iRow]])
                
                del lstMutate[:]            
                
#            self.raw_pref.getDf().to_csv(OutputFilePath, encoding='utf-8', index=True)                    
        return self.WriteToDirectory(OutputFilePath, Percentage, MutateType)    
    # Mutation Percentage should be < 1
    #Mutate votes on extremes when MutateType == 0, else muatate votes in the middle
    #Extremes means the first two and the last two
    #votes in the middle means the rest six  
    
    def WriteToDirectory(self, OutPath, MutationPercentage, MutationType):
        OutputDirectory = OutPath + "/Mutation" + "_" + str(MutationPercentage) + "_" + str(MutationType) + str(self.index) + ".csv"
        self.raw_pref.getDf().to_csv(OutputDirectory, encoding='utf-8', index=True)  
        
        return OutputDirectory                  
           
    def GetResult(self, MutationPercentage, MutationType, OutputDirectory):
        
        OutputDirectory = self.GenerateRandom(MutationPercentage, MutationType, OutputDirectory)
        
        return OutputDirectory

        

        
        
        
    
