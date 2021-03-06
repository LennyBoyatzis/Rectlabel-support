# https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py
# Replace the code at Line 268
# m = maskUtils.decode(rle)
# with the code below
# m = maskUtils.decode(rle)
# m_shape = m.shape
# m = np.ravel(m, order='F')
# m = m.reshape(m_shape, order='C')

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import pprint
pp = pprint.PrettyPrinter(indent=2)
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

imgFolder = '/Users/ryo/Desktop/test_annotations/test_data_coco/'
annFile='/Users/ryo/Desktop/test_annotations/test_data_coco/annotations.json'

coco=COCO(annFile)
imgIds = coco.getImgIds(imgIds = [1, 2])
img = coco.loadImgs(imgIds[0])[0]
I = io.imread(imgFolder + img['file_name'])
plt.axis('off')
plt.imshow(I);

catIds = list(range(1, 100))
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)

for id, ann in enumerate(anns):
    bb = ann['bbox']
    x1, x2, y1, y2 = [bb[0], bb[0]+bb[2], bb[1], bb[1]+bb[3]]
    ann['segmentation'] = [[x1, y1, x1, y2, x2, y2, x2, y1]]
pp.pprint(anns)

coco.showAnns(anns)
plt.show()

