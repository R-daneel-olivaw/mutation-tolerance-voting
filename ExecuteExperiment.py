'''
Created on Mar 5, 2015

@author: Akshat
'''

def executeExp():
    pr = SushiReader('D:\Lectures\Winter2015\CS886\Project\sushi3_preflib\sushi3_preflib\ED-00015-00000001.soc')
    pr.loadUp()
    df = pr.getDf()

    print(df)

if __name__ == '__main__':
    from code.prefreaders import SushiReader
    executeExp()