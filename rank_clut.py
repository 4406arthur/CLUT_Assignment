import numpy as np
import sys
import cv2
import json
from scipy.stats import itemfreq



class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray) and obj.ndim == 1:
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a, counts = np.unique(a.view([('', a.dtype)]*a.shape[1]),return_counts=True)
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1])), counts

#test_a = np.array([[1, 1, 1], [2, 3,3], [1, 1,1], [5, 4,3], [2, 3,2]])



img = np.array(cv2.imread(sys.argv[1]))

table = []
for each_pixel in img:
	#print each_pixel
	table.extend(each_pixel)

table, counts = unique_rows(table)


clut=[]
for clut_pixel in range(256):
	#print counts.argmax()
 	clut.append(table[counts.argmax()])
 	table = np.delete(table,counts.argmax(),0)
 	counts = np.delete(counts,counts.argmax())


print 'done'

ans = json.dumps(clut,cls=NumpyAwareJSONEncoder)
fo = open('clut','w')
fo.write(ans)
fo.close()

