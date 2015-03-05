'''
Created on Mar 5, 2015

@author: Akshat
'''
from pandas.core.frame import DataFrame

# 'ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki'

def executeExp():
    pr = SushiPref('D:\Lectures\Winter2015\CS886\Project\sushi3_preflib\sushi3_preflib\ED-00015-00000001.soc')
    pr.loadUp()

    #print(df)
    
    pu = SushiPrefUtil(pr)
    
    prefEbi = pu.getCount('ebi')
    prefAnago = pu.getCount('anago')
    prefMaguro = pu.getCount('maguro')
    prefIka = pu.getCount('ika')
    prefUni = pu.getCount('uni')
    prefSake = pu.getCount('sake')
    prefTamago = pu.getCount('tamago')
    prefToro = pu.getCount('toro')
    prefTekkaMaki = pu.getCount('tekka-maki')
    prefKappaMaki = pu.getCount('kappa-maki')
    
    #print('Ebi', prefEbi)
    #print('Anago', prefAnago)
    
    # fullPref = pd.concat([prefEbi,prefAnago], axis=1)
    fullPref = DataFrame(dict(s1=prefEbi, s2=prefAnago, s3=prefMaguro, s4=prefIka, s5=prefUni, s6=prefSake, s7=prefTamago, s8=prefToro, s9=prefTekkaMaki, s10=prefKappaMaki))
    fullPref.columns = ['ebi', 'anago', 'maguro', 'ika', 'uni', 'sake', 'tamago', 'toro', 'tekka-maki', 'kappa-maki']
    fullPref.index.name = 'Rank#'
    
    print('RESULTS...')
    print(fullPref)

if __name__ == '__main__':
    from code.prefreaders import SushiPref
    from code.prefUtil import SushiPrefUtil
    executeExp()
