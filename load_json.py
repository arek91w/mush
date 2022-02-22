import json
import cv2
 
# Opening JSON file
f = open('via_project_15May2020_15h35m (3).json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
'''
for i in data['emp_details']:
    print(i)
 '''

image = cv2.imread('17.jpg')
im_2 = cv2.imread('17.jpg')

for i in data['_via_img_metadata']['17.jpg345211']['regions']:
    print(len(i['shape_attributes']['all_points_x']))
    print(len(i['shape_attributes']['all_points_y']))
    for z, y in zip((i['shape_attributes']['all_points_x']), (i['shape_attributes']['all_points_y'])):
        print(z, y)
        image = cv2.circle(image, (z, y), 1, (0, 0, 255), 2)
# Closing file
f.close()


cv2.imshow('im', image)
#cv2.waitKey(0)

mask1 = cv2.inRange(im_2, (66, 66, 66), (255, 255,255))

cv2.imshow('mask', mask1)
cv2.waitKey(0)