import cv2
import numpy
import json
import sys
import scipy
from PIL import Image

with open('color_table.json') as color_table_file:
    color_table = json.load(color_table_file)
 
    datas = []
 
    for color in color_table:
        datas.append([float(num) for num in color.split(',')])
 
    color_table = numpy.array(datas)


with open('result') as target_img:
    img_index = numpy.array(json.load(target_img))
    

img = []

for idx_of_row, row in enumerate(img_index):
    newRow = []
    #print idx_of_row, row
    for color_index in row:
        newRow.append(color_table[color_index])

    img.append(newRow)

buf = numpy.array(img)

ans = buf.astype(numpy.uint8)

result = Image.fromarray(ans)

result.save('ans.bmp')