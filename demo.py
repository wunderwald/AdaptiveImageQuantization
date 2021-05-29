from os import error
from PIL import Image
from quantize import quantize
from pathlib import Path

def parameterization():
    img = Image.open("./demoInput.jpg")
    pixels = img.load()
    dims = img.size

    minCellDims = [6, 6]

    if(dims[0] != dims[1]):
        error("The code currently only works for sqaure images.")

    for thresh in [ 690, 6900, 42000, 420000, 690000 ]:
        for edgeType in [ "inv", "black", "white" ]:
            out = Image.new(mode="RGB", size=dims)
            quantize(
                cell=[ 0, 0, dims[0], dims[1] ], 
                inputPixels=pixels, 
                outputImage=out, 
                thresh=thresh, 
                minCellDims=minCellDims,
                showEdges=True, 
                edgeType=edgeType
            )
            path = Path("./demoOut/out_{thresh}_{edge}_min{w}x{h}.png".format(thresh=thresh, edge=edgeType, w=minCellDims[0], h=minCellDims[1]))
            out.save(path)
            out.close()

def test():
    img = Image.open("./laikka.jpg")
    pixels = img.load()
    dims = img.size

    minCellDims = [6, 6]

    thresh = 69420

    for edgeType in [ "inv", "black", "white" ]:
        out = Image.new(mode="RGB", size=dims)
        quantize(
            cell=[ 0, 0, dims[0], dims[1] ], 
            inputPixels=pixels, 
            outputImage=out, 
            thresh=thresh, 
            minCellDims=minCellDims,
            showEdges=True, 
            edgeType=edgeType
        )
        path = Path("./demoOut/out_{thresh}_{edge}_min{w}x{h}.png".format(thresh=thresh, edge=edgeType, w=minCellDims[0], h=minCellDims[1]))
        out.save(path)
        out.close()
