import cv2
from sklearn.cluster import KMeans
from scipy.io import wavfile
import numpy as np
class AudioSeperation:
#	def andrewOwens(self, videoInput):
#		#return foregroundAudio,backgroundAudio
#        return 0
#    
#	def system_1(self, foregroundAudio, backgroundAudio, index):
#        outputAudio = 0
#		return outputAudio
    
    def clustering(self, audiofile):
        rate,X = wavfile.read(audiofile)
        kmean = KMeans(n_clusters = 4)
        kmean.fit(np.abs(X))
        pr = kmean.predict(X)
        centers = kmean.cluster_centers_                 
        return pr,centers,X,rate   
