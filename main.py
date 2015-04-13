import cv2
import numpy
import json
import sys
import math
import colormath
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


def shortPixel(target_color, color_table):
    buf = []
    buf2 = []
    ans = []
    big_RGB   = target_color.argmax()
    numpy.delete(target_color, big_RGB)
    mid_RGB   = target_color.argmax()
    numpy.delete(target_color, mid_RGB)
    small_RGB = target_color.argmax()
    numpy.delete(target_color, small_RGB)
    for color in color_table:
        tmp = math.fabs(target_color[small_RGB]-color[small_RGB])
        if (tmp < 200 ):
            buf.append(tmp)
    for index in buf:
        tmp = math.fabs(target_color[mid_RGB]-color_table[index][mid_RGB])
        if (tmp < 150 ):
            buf2.append(tmp)
    for index in buf2:
        ans.append(math.fabs(target_color[big_RGB]-color_table[index][big_RGB]))

    return ans.index(min(ans))

def ColourDistance(e1, e2 ):
    rmean = ( e1[0] + e2[0] ) / 2
    r = e1[0] - e2[0]
    g = e1[1] - e2[1]
    b = e1[2] - e2[2]
    return math.sqrt((((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8));





def ShortestIndex(target_color, color_table):
    distances = []

    for color in color_table:
        # R = int(color[0] - target_color[0])
        # G = int(color[1] - target_color[1])
        # B = int(color[2] - target_color[2])

        # R_square = math.pow(R, 2)
        # G_square = math.pow(G, 2)
        # B_square = math.pow(B, 2)

        # distances.append(math.sqrt(R_square + G_square + B_square))
        distances.append(ColourDistance(target_color,color))
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
result = bytearray(result)
#print newImg
fo = open('result','wb')
fo.write(result)
fo.close()
# cv2.imwrite('result', numpy.array(newImg))
