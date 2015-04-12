import cv2
import numpy
import json
import sys
import math
from collections import Counter
from scipy.spatial import distance



with open('clut') as color_table_file:
    color_table = numpy.array(json.load(color_table_file))   

    
img = numpy.array(cv2.imread(sys.argv[1]))

 # Usage: Find the color in color_table which has the shortest distance between target_color
#
# Example:
# target_color = [155, 201, 301]
# color_table = [[1, 2, 3], [4, 5, 6]]
def ShortestIndex(target_color, color_table):
    distances = []
 
    for color in color_table:
        R = int(color[0] - target_color[0])
        G = int(color[1] - target_color[1])
        B = int(color[2] - target_color[2])
 
        R_square = math.pow(R, 2)
        G_square = math.pow(G, 2)
        B_square = math.pow(B, 2)
 
        distances.append(math.sqrt(R_square + G_square + B_square))
 
    return distances.index(min(distances))
 
newImg = []
 
for idx_of_row, row in enumerate(img):
    newRow = []
    for color in row:
        newRow.append(ShortestIndex(color, color_table))
 
    sys.stdout.write('\r'+str(idx_of_row)+'/'+str(len(img)))
    sys.stdout.flush()
 
    newImg.append(newRow)


result = json.dumps(newImg)


fo = open('result','w')
fo.write(result)
fo.close()
#cv2.imwrite('result', numpy.array(newImg))
