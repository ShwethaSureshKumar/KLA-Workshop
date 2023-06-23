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

total_defects=[]

for i in range(1,16):
    if i ==15:
        img1=PIL.Image.open("wafer_image_{0}.png".format(15))
        img2=PIL.Image.open("wafer_image_{0}.png".format(1))
    else:
        img1=PIL.Image.open("wafer_image_{0}.png".format(i))
        img2=PIL.Image.open("wafer_image_{0}.png".format(i+1))
    dif=PIL.ImageChops.difference(img1, img2)
    dif=dif.convert('RGB')
    pixels=dif.load()
    
    defect_points=[]
    
    for y in range(height):
        for x in range(width):
            #if x in [range(care_area_coords['x_start_1'],care_area_coords['x_stop_1']),range(care_area_coords['x_start_2'],care_area_coords['x_stop_2']),range(care_area_coords['x_start_3'],care_area_coords['x_stop_3'])] or (x not in [range(exclusion_zones['x_start_1'],exclusion_zones['x_stop_1']),range(exclusion_zones['x_start_2'],exclusion_zones['x_stop_2']),range(exclusion_zones['x_start_3'],exclusion_zones['x_stop_3'])]) or y in [range(care_area_coords['y_start_1'],care_area_coords['y_stop_1']),range(care_area_coords['y_start_2'],care_area_coords['y_stop_2']),range(care_area_coords['y_start_3'],care_area_coords['y_stop_3'])] or (y not in [range(exclusion_zones['y_start_1'],exclusion_zones['y_stop_1']),range(exclusion_zones['y_start_2'],exclusion_zones['y_stop_2']),range(exclusion_zones['y_start_3'],exclusion_zones['y_stop_3'])]):
            #if x in [range(care_area_coords['x_start_1'],care_area_coords['x_stop_1']),range(care_area_coords['x_start_2'],care_area_coords['x_stop_2']),range(care_area_coords['x_start_3'],care_area_coords['x_stop_3'])] or (y in [range(care_area_coords['y_start_1'],care_area_coords['y_stop_1']),range(care_area_coords['y_start_2'],care_area_coords['y_stop_2']),range(care_area_coords['y_start_3'],care_area_coords['y_stop_3'])]):
                colour=pixels[x,y]
                if colour !=(0,0,0):
                    defect_points.append((i,x,height-y-1))
            #print(1,x,y)
    total_defects.append(defect_points)
    
with open("output5.csv","a+") as csvfile:
    csvwriter=csv.writer(csvfile)
    for i in total_defects:
        csvwriter.writerows(i)