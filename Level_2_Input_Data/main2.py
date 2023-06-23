# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:46:45 2023

@author: shwet
"""

"""
LOGIC:
find intersection of image with every other image.
with that find whether anomaly or not.
if it is present in all remove it from other lists.

 """ 

from PIL import Image
import csv

#import json file 
import json
f=open('input.json')
data=json.load(f)
width=data['die']['width']
height=data['die']['height']
colour_count={}
#setting care area and exclusion zone coordinates

care_area_coords={}
exclusion_zones={}
for i in range(len(data['care_areas'])):
    care_area_coords['x_start_{0}'.format(i+1)]=data['care_areas'][i]['top_left']['x']
    care_area_coords['x_stop_{0}'.format(i+1)]=data['care_areas'][i]['bottom_right']['x']
    care_area_coords['y_start_{0}'.format(i+1)]=data['care_areas'][i]['bottom_right']['y']
    care_area_coords['y_stop_{0}'.format(i+1)]=data['care_areas'][i]['top_left']['y']
    exclusion_zones['x_start_{0}'.format(i+1)]=data['exclusion_zones'][i]['top_left']['x']
    exclusion_zones['x_stop_{0}'.format(i+1)]=data['exclusion_zones'][i]['bottom_right']['x']
    exclusion_zones['y_start_{0}'.format(i+1)]=data['exclusion_zones'][i]['bottom_right']['y']
    exclusion_zones['y_stop_{0}'.format(i+1)]=data['exclusion_zones'][i]['top_left']['y']
    
print(care_area_coords)
print(exclusion_zones)

for i in range(1,2):#change stop val to 16
    img=Image.open("wafer_image_{0}.png".format(i))
    img=img.convert('RGB')
    pixels=img.load()
    for y in range(height):
        for x in range(width):
            colour=pixels[x,y]
            if colour in colour_count:
                colour_count[colour]+=1
            else:
                colour_count[colour]=1

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
    
    
for j in range
# colour_count={}

# for i in range(1,16):#change stop as 6
#     img=Image.open("wafer_image_{0}.png".format(i))
#     img=img.convert('RGB')
#     pixels=img.load()
#     #print(pic[0,0])
    
    
#     #iterating through each pixel to find the majority colour( ie bg)
#     for y in range(y_start,y_stop):
#         for x in range(x_start,x_stop):
#             colour=pixels[x,y]
#             if colour in colour_count:
#                 colour_count[colour]+=1
#             else:
#                 colour_count[colour]=1
#     #print(colour_count)
#     #print(max(colour_count.values()))
    
    
#     major={} 
#     #for finding bg grey
#     maxcol1=max(colour_count.values())
#     for key in colour_count:
#         if colour_count[key]==maxcol1:
#             major_col1=key
#     major[major_col1]=colour_count.pop(major_col1)
   
    
#     #for finding white line
#     maxcol2=max(colour_count.values())
#     for key in colour_count:
#         if colour_count[key]==maxcol2:
#             major_col2=key
#     major[major_col2]=colour_count.pop(major_col2)
#     #print(major)
    
#     defect_points=[]
#     for y in range(y_start,y_stop):
#         for x in range(x_start,x_stop):
#             colour=pixels[x,y]
#             if colour!= major_col1 and colour!=major_col2:
#                 defect_points.append((i,x,y_stop-y-1))
#     #print(defect_points)
    
    
#     #writing into file
#     with open("output2.csv","a+") as csvfile:
#         csvwriter=csv.writer(csvfile)
#         csvwriter.writerows(defect_points)