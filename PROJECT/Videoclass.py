# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:36:13 2019

@author: Abhilash
"""
import subprocess
from scipy.io import wavfile
from moviepy.editor import *
import ffmpeg

import os

import numpy as np
from matplotlib import pyplot as plt

class Video:
    def __init__(self,Videosourceloaction):
        self.Videosourceloaction = Videosourceloaction

    def CropVideo(self,start,stop):
        cropclip = VideoFileClip(self.Videosourceloaction).subclip(start,stop)
        return cropclip

    def readvideofile(self):
        clip = VideoFileClip(self.Videosourceloaction)
        return clip

    def readandwritecropvideo(self,start,stop,filenametobesavedfrocropvideo):
        cropclip = self.CropVideo(start,stop)
        cropclip.write_videofile(filenametobesavedfrocropvideo)

    def getaudiofromoriginalvideoandwrite(self,whichfile):
        audio = VideoFileClip(self.Videosourceloaction).audio
        audio.write_audiofile(self.Videosourceloaction+whichfile)
        #return self.Videosourceloaction+'original.wav'

                

