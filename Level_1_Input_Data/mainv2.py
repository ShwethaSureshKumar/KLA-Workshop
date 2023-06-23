# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:01:23 2023

@author: shwet
"""

"""
LOGIC:
find bg colour
choose pixels which differ from bg colour
and which are not the colour of the lines
find coordinates of pixels
find which image
write into csv file
 """ 

from PIL import Image
import csv

#import json file 
import json
f=open('input.json')
data=json.load(f)

#setting care area coordinates
x_start=data['care_areas'][0]['top_left']['x']
x_stop=data['care_areas'][0]['bottom_right']['x']
y_start=data['care_areas'][0]['bottom_right']['y']
y_stop=data['care_areas'][0]['top_left']['y']

colour_count={}
defect_list=[]

for i in range(1,6):#change stop as 6
    img=Image.open("wafer_image_{0}.png".format(i))
    img=img.convert('RGB')
    pixels=img.load()
    #print(pic[0,0])
    
    
    #iterating through each pixel to find the majority colour( ie bg)
    for y in range(y_start,y_stop):
        for x in range(x_start,x_stop):
            colour=pixels[x,y]
            if colour in colour_count:
                colour_count[colour]+=1
            else:
                colour_count[colour]=1
    #print(colour_count)
    #print(max(colour_count.values()))
    
    
    major={} 
    #for finding bg grey
    maxcol1=max(colour_count.values())
    for key in colour_count:
        if colour_count[key]==maxcol1:
            major_col1=key
    major[major_col1]=colour_count.pop(major_col1)
   
    
    #for finding white line
    maxcol2=max(colour_count.values())
    for key in colour_count:
        if colour_count[key]==maxcol2:
            major_col2=key
    major[major_col2]=colour_count.pop(major_col2)
    #print(major)
    
    defect_points=[]
    defect_xy=[]
    for y in range(y_start,y_stop):
        for x in range(x_start,x_stop):
            colour=pixels[x,y]
            if colour!= major_col1 and colour!=major_col2:
                defect_points.append((i,x,y_stop-y-1))
                defect_xy.append((x,y_stop-y-1))
                
                
#check every image with every other image
    #print(defect_points)
    
    
    #writing into file
    # with open("output.csv","a+") as csvfile:
    #     csvwriter=csv.writer(csvfile)
    #     csvwriter.writerows(defect_points)