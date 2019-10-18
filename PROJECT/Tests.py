from AudioSeperation import AudioSeperation
from Videoclass import Video
import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt

def test1(AudioSeperationObject):
    video = Video('Test.mp4')
    print('here')
    #video.getaudiofromoriginalvideoandwrite('original.wav')
    aa = video.Videosourceloaction+'original.wav'
    ss = AudioSeperation()
    out,centres,X,rate = ss.clustering(aa)
    
    
    return out,centres,X,rate
    

#if '__name__' == '__main__':
ss = AudioSeperation()    
out,centres,X,rate = test1(ss)
print(out)
def makechangesonoriginalvideo(X,out,rate,filename):
    newaudio = np.multiply(X[:,0],out)
    newaudio1 = np.append(newaudio,newaudio)
    newaudio1 = np.reshape(newaudio1,(len(newaudio),2))
    wavfile.write(filename,rate,newaudio1)
    return newaudio1 

audio = makechangesonoriginalvideo(X,out,rate,'new.wav')    

a = np.arange(1,4854088,1)
#
plt.scatter(a,X[:,0],c=out, s=50, cmap='viridis')
#plt.scatter()
#
#plt.plot(X[:,0][0:10000])