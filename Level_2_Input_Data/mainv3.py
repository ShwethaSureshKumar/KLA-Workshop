# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:11:42 2023

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
img2=PIL.Image.open("wafer_image_2.png")

dif=PIL.ImageChops.difference(img1, img2)
dif=dif.convert('RGB')
pixels=dif.load()

defect_points=[]

for y in range(height):
    for x in range(width):
        colour=pixels[x,y]
        if colour !=(0,0,0):
            defect_points.append((1,x,height-y-1))
            #print(1,x,y)

with open("output2.csv","a+") as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerows(defect_points)
        