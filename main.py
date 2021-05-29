# define max and min square size
# split image into cells of max size
# for each cell: 
#  -> if standard deviation < thresh: mark as done, set color to average or median
#  -> else: split cell into 4 new cells, call recursion

from os import error
from PIL import Image
from quantize import quantize


img = Image.open("./input.jpg")
pixels = img.load()
dims = img.size

if(dims[0] != dims[1]):
    error("The code currently only works for sqaure images.")

for thresh in [ 690, 4200, 6900, 42000, 420000, 690000 ]:
    for edgeType in [ "inv", "black", "white" ]:
        out = Image.new(mode="RGB", size=dims)
        quantize(
            cell=[ 0, 0, dims[0], dims[1] ], 
            inputPixels=pixels, 
            outputImage=out, 
            thresh=thresh, 
            showEdges=True, 
            edgeType=edgeType
        )
        out.save("./out_{thresh}_{edge}.jpg".format(thresh=thresh, edge=edgeType))
        out.close()



