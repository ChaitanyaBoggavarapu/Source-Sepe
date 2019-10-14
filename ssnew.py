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

rate2,test_audio = wavfile.read('Test.wav','w')
rate,bg_audio = wavfile.read('bg_Test.wav')
rate1,fg_audio = wavfile.read('fg_Test.wav')



fg = fg_audio[:,0]
fg = np.asarray(fg)
bg = bg_audio[:,0]
bg = np.asarray(bg)


z = []
y = []

test = test_audio
testnew = test_audio
test = np.asarray(test)
testnew = np.asarray(testnew)
for i in range(0,len(test_audio),44100):
    
    a = np.sum(np.abs(fg[i:i+44100])) 
    z.append(a)
    b = np.sum(np.abs(bg[i:i+44100]))
    y.append(b)
    if (a>=b):
        print ('infi')
        test[i:i+44100] = 1*test[i:i+44100] 
        # fgnew.append(fg[i:i+44100])
    if(a<b):     
        if(len(str(a))==len(str(b)) and (b-a)>a):
            test[i:i+44100] = 1*test[i:i+44100] 
        else:
            print ('inelse')
            test[i:i+44100] = 0*test[i:i+44100] 
        
wavfile.write('xyznewzxxc.wav',rate2,test)        
