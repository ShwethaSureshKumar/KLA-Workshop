# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:07:12 2023

@author: shwet
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:34:38 2023

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

total_defects=[]
actual_total_defects=[]
coords=[]
for i in range(1,16):
    for j in range(1,16):
        if i !=j:
            img1=PIL.Image.open("wafer_image_{0}.png".format(i))
            img2=PIL.Image.open("wafer_image_{0}.png".format(j))
            dif=PIL.ImageChops.difference(img1,img2)
            dif=dif.convert('RGB')
            pixels=dif.load()
            
            defect_points=[]
            
            for y in range(height):
                for x in range(width):
                    colour=pixels[x,y]
                    if colour !=(0,0,0):
                        coords.append((i,x,height-y-1))
                        defect_points.append((x,height-y-1))
                    #print(1,x,y)
            total_defects.append(defect_points)

total_defects=[set(i) for i in total_defects]

actual_total_defects.append(total_defects[0])
for i in total_defects:
    actual_total_defects[0] &=i

with open("output6.csv","a+") as csvfile:
    csvwriter=csv.writer(csvfile)
    for i in actual_total_defects:
        csvwriter.writerows(i)