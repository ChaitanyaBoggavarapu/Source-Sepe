# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 00:33:45 2019

@author: Abhilash
"""
import subprocess
from scipy.io import wavfile
from moviepy.editor import *
import ffmpeg

import os

print(os.path)

clip = VideoFileClip('C:/Users/Abhilash/Desktop/Sourceseperation/fg_Test.mp4')


audio = clip.audio

audio.write_audiofile('fg_Test.wav')


clip2 = VideoFileClip('C:/Users/Abhilash/Desktop/Sourceseperation/bg_Test.mp4')

audio1 = clip2.audio

audio1.write_audiofile('bg_Test.wav')


origclip = VideoFileClip('C:/Users/Abhilash/Desktop/Sourceseperation/Test.mp4').subclip(0,33)



audioorig = origclip.audio

audioorig.write_audiofile('Test.wav')

rate,bg_audio = wavfile.read('bg_Test.wav')
rate1,fg_audio = wavfile.read('fg_Test.wav')

rate2,test_audio = wavfile.read('Test.wav','w')

bg = bg_audio[:,0]
fg = fg_audio[:,0]
te = test_audio[:,0]


new = te*bg[0:len(te)]

NEW = (new / te)
NEW = NEW.astype(int)
wavfile.write("new.wav",rate,new)

import numpy as np
NEW = np.nan_to_num(NEW)

len(NEW)
wavfile.write("new.wav",rate,NEW)

from matplotlib import pyplot as plt
plt.plot(bg_audio,'r')
plt.plot(test_audio,'b')
plt.plot(fg_audio,'g')

fgnew = []
count = 0
count1 = 0
import numpy as np
fg = fg_audio[:,0]
fg = np.asarray(fg)
bg = bg_audio[:,0]
bg = np.asarray(bg)

zers = np.zeros(44100)
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
    if (a>=b or (a-b)<100000):
         fgnew.append(fg[i:i+44100])
    else:
         test[i:i+44100] = 0*test[i:i+44100] 

plt.plot(fg)
plt.plot(bg)

nx = np.average(z)
ny = np.average(y)

for i in range(0,len(test_audio),44100):
    
    a = np.sum(np.abs(fg[i:i+44100])) 
    #z.append(a)
    b = np.sum(np.abs(bg[i:i+44100]))
    #y.append(b)
    if (a>=nx or b>ny):
         fgnew.append(fg[i:i+44100])
    else:
         testnew[i:i+44100] = 0*testnew[i:i+44100] 


xyz = np.asarray(fgnew)
xyz = xyz.reshape(34*44100).astype(int)

abc = np.append(xyz[0:1455300],xyz[0:1455300])
abc = abc.reshape(1455300,2)
plt.plot(abc)
plt.plot(bg_audio[:,0],'g')
plt.plot(fg_audio[:,0],'b')

lml = np.multiply(fg[0:1455300],xyz[0:1455300])

wavfile.write('xyznew.wav',rate,lml)

wavfile.write('xyznewzxxc.wav',rate,test)

wavfile.write('omg.wav',rate,testnew)



wavfile.write('xyz.wav',rate,abc)

tt = fg_audio - bg_audio

a = np.array([[1,2],[2,4],[3,6],[4,5]])

a[1:3] =0 


###On background using foreground
xt = np.abs(bg_audio) - np.abs(fg_audio)
yt = np.abs(fg_audio) - np.abs(bg_audio)
wavfile.write('sxxt.wav',rate,xt)
wavfile.write('sxyt.wav',rate,yt)

plt.plot(yt)
plt.plot(xt)
for i in range(0,len(test_audio),88200):
    
    a = np.sum(np.abs(yt[i:i+88200])) 
    
    #z.append(a)
    b = np.sum(np.abs(xt[i:i+88200]))
    print(a,b)
    #y.append(b)
    if (a>=nx):
         #fgnew.append(fg[i:i+44100])
         print('in if')
    else:
         print('in else')   
         test[i:i+88200] = 0*test[i:i+88200] 
wavfile.write('fg-bg.wav',rate,test)