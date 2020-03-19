# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 01:33:54 2019

@author: Abhilash
"""

import subprocess
from scipy.io import wavfile
from moviepy.editor import *
import ffmpeg

import os

import numpy as np
from matplotlib import pyplot as plt

rate2,src_audio = wavfile.read('Test.wav','w')
rate,bg_audio = wavfile.read('bg_Test.wav')
rate1,fg_audio = wavfile.read('fg_Test.wav')



fg = fg_audio[:,0]
fg = np.asarray(fg)
bg = bg_audio[:,0]
bg = np.asarray(bg)


z = []
y = []

test = src_audio
testnew = src_audio
test = np.asarray(test)
testnew = np.asarray(testnew)
ones = np.ones(11500)
zeros = np.zeros(11500)
fg_array = []
bg_array = []
misc_array = []
for i in range(0,len(test_audio),11500):
    countfg = 0
    countbg = 0
    countun = 0
    for j in range(i,i+11500,1):
        if (fg[i]>bg[i]):
            countfg=countfg+1
        else:
            countbg = countbg+1

    if (countfg/11500>0.7):
        fg_array.append[ones]
        bg_array.append[zeros]
        misc_array.append[zeros]    
        print(countfg)
    elif(countfg/11500<0.3):
        fg_array.append[zeros]
        bg_array.append[ones]
        misc_array.append[zeros]
    else:
        fg_array.append[zeros]
        bg_array.append[zeros]
        misc_array.append[ones]


testnew = fg_array*testnew
        
wavfile.write('xyznewzxxc.wav',rate2,testnew)        
