# -*- coding: utf-8 -*-
import cv2
import os, sys
import glob
import random as rand


def videoToImages(videoPath, label, num): 
    
    vidcap = cv2.VideoCapture(videoPath)
    success,image = vidcap.read()
    
    print(f'video read success: {success}' )
    
    count = 0
    while success:
        if (count % 10 ) == 0:
          cv2.imwrite(f'./Dataset/train/{label}/{label}img{num}.jpg',image)  
          num += 1     
    
        elif (count % 33) == 0:
         cv2.imwrite(f'./Dataset/test/{label}/{label}img{num}.jpg',image)  
         num += 1
        
        elif (count % 457) == 0:
         cv2.imwrite(f'./Dataset/val/{label}/{label}img{num}.jpg',image)  
         num += 1
    
        success,image = vidcap.read()
        count +=1
    
    return num

def keyVidToImg():
    num = 0
    for file in glob.glob(f'./KeyVideos/*.mp4'):
        print(file)
        num = videoToImages(file,'Key', num)
    
    print(num)
    
def noKeyVidToImg():
    num = 0
    for file in glob.glob(f'./NoKeyVideos/*.mp4'):
        print(file)
        num = videoToImages(file, 'NoKey', num)
        
    print(num)

keyVidToImg()
noKeyVidToImg()
