# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:28:43 2023

@author: shwet
"""

import PIL
import csv

#import json file 
import json
f=open('input.json')
data=json.load(f)
width=data['die']['width']
height=data['die']['height']

img1=PIL.Image.open("wafer_image_1.png")
#img2=PIL.Image.open("wafer_image_2.png")

#dif=PIL.ImageChops.difference(img1, img2)
#dif=dif.convert('RGB')
#pixels=dif.load()

img=[]
#difference for wafer1 with wafer2 and wafer3
for i in range(2,4):
    img2=PIL.Image.open("wafer_image_{0}.png".format(i))
    dif=PIL.ImageChops.difference(img1, img2)
    dif=dif.convert('RGB')
    img.append(dif)

defect_points=[]
for i in range(2,4):
    for y in range(height):
        for x in range(width):
            colour=pixels[x,y]
            if colour !=(0,0,0):
                defect_points.append((1,x,height-y-1))
            #print(1,x,y)

#set intersect code

with open("output2.csv","a+") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerows(defect_points)