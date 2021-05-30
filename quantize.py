import math

def sumOfSquares(pixels, cell, avgPixel):
    sum = 0
    for y in range(cell[1], cell[3]):
        for x in range(cell[0], cell[2]):
            sum += math.pow(pixels[x, y][0] - avgPixel[0], 2)
            sum += math.pow(pixels[x, y][1] - avgPixel[1], 2)
            sum += math.pow(pixels[x, y][2] - avgPixel[2], 2)
    return sum

def avg(pixels, cell):
    numPixels = (cell[2]-cell[0]) * (cell[3]-cell[1])
    avgPixel = [0, 0, 0]
    for y in range(cell[1], cell[3]):
        for x in range(cell[0], cell[2]):
            avgPixel[0] += pixels[x, y][0] / numPixels
            avgPixel[1] += pixels[x, y][1] / numPixels
            avgPixel[2] += pixels[x, y][2] / numPixels
    return (
        math.floor(avgPixel[0]),
        math.floor(avgPixel[1]),
        math.floor(avgPixel[2]),
    )
def inv(pixel):
    return (
        255 - pixel[0],
        255 - pixel[1],
        255 - pixel[2]
    )

def limit(value, range):
    if(value < range[0]):
        return range[0]
    if(value > range[1]):
        return range[1]
    return value

def brightness(color, factor):
    r = math.floor(color[0] * factor)
    g = math.floor(color[1] * factor)
    b = math.floor(color[2] * factor)
    return (
        limit(r, [0, 255]),
        limit(g, [0, 255]),
        limit(b, [0, 255]),
    )

def getEdgeColor(edgeType, avgColor):
    if(edgeType not in [ "inv", "black", "white", "darken", "lighten" ]):
        print("Invalid edge Type. Options are inv, black, white. Black is used as default. ")
    if(edgeType == 'inv'):
        return inv(avgColor)
    if(edgeType == 'black'):
        return (0, 0, 0)
    if(edgeType == 'white'):
        return (255, 255, 255)
    if(edgeType == 'darken'):
        return brightness(avgColor, .69)
    if(edgeType == 'lighten'):
        return brightness(avgColor, 1.21)
    return (0, 0, 0)
    

def subdivideQuad(cell, dims, inputPixels, outputImage, thresh, minCellDims, showEdges, edgeType):
    [ width, height ] = dims
    halfWidth = math.floor(width / 2)
    halfHeight = math.floor(height / 2)
    cell0 = [ cell[0], cell[1], cell[0] + halfWidth, cell[1] + halfHeight]
    cell1 = [ cell[0] + halfWidth, cell[1], cell[2], cell[1] + halfHeight]
    cell2 = [ cell[0], cell[1] + halfHeight, cell[0] + halfWidth, cell[3]]
    cell3 = [ cell[0] + halfWidth, cell[1] + halfHeight, cell[2], cell[3]]
    quantize(cell0, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, minCellDims=minCellDims, showEdges=showEdges, edgeType=edgeType)
    quantize(cell1, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, minCellDims=minCellDims, showEdges=showEdges, edgeType=edgeType)
    quantize(cell2, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, minCellDims=minCellDims, showEdges=showEdges, edgeType=edgeType)
    quantize(cell3, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, minCellDims=minCellDims, showEdges=showEdges, edgeType=edgeType)


def quantize(cell, inputPixels, outputImage, thresh, minCellDims = [2,2], showEdges=True, edgeType="black"):

    width = cell[2] - cell[0]
    height = cell[3] - cell[1]

    # write original pixels for cells of less than 2x2 px
    if(width <= minCellDims[0] or height <= minCellDims[1] or width <= 2 or height <= 2):
        for y in range(cell[1], cell[3]):
            for x in range(cell[0], cell[2]):
                outputImage.putpixel(xy=(x, y), value=inputPixels[x, y])
        return

    # if deviation is under threshold, paint the cell in the average color
    avgColor = avg(pixels=inputPixels, cell=cell)
    deviation = sumOfSquares(pixels=inputPixels, cell=cell, avgPixel=avgColor)
    if(deviation <= thresh):
        for y in range(cell[1], cell[3]):
            for x in range(cell[0], cell[2]):
                if(showEdges and (x==cell[0] or y==cell[1] or x==cell[2]-1 or y==cell[3]-1)):
                    edgeColor = getEdgeColor(edgeType=edgeType, avgColor=avgColor)
                    outputImage.putpixel(xy=(x, y), value=edgeColor)
                else:    
                    outputImage.putpixel(xy=(x, y), value=avgColor)
        return
    
    # if deviation is largen than threshold, subdivide cell and quantize subdivisions
    subdivideQuad(
        cell=cell, 
        dims=[ width, height ],
        inputPixels=inputPixels,
        outputImage=outputImage,
        thresh=thresh,
        minCellDims=minCellDims,
        showEdges=showEdges,
        edgeType=edgeType
    )


