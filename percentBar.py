# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:01:30 2020

@author: Chiakai
"""

def percentBar(percent=0, showPercent=True, showLen=1):
    bar = ''
    
    percent100 = round(percent*100)
    percent100_show = round(percent* 100, showLen) 
    #print(f'percent100 = {percent100}')
    
    nowTEN = percent100 // 10
    #print(f'nowTEN = {nowTEN}')
    
    bar = '▉' * nowTEN
    
    nowONE = percent100 % 10
    #print(f'nowONE = {nowONE}')
    
    if nowONE == 1:
        bar += '▏'
    elif nowONE in [2,3]:
        bar += '▎'
    elif nowONE in [4,5]:
        bar += '▍'
    elif nowONE in [6,7]:
        bar += '▋'
    elif nowONE in [8,9]:
        bar += '▊'
    
    if showPercent:
        bar = f'{bar}({percent100_show}%)'
    return bar

if __name__ == '__main__':
    import time
    for i in range(1001):
        
        percent = i * 0.001
    
        bar = percentBar(percent)
    
        print(bar, end='\r')
        time.sleep(0.001)