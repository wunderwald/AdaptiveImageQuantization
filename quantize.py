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

def quantize(cell, inputPixels, outputImage, thresh, showEdges=False, edgeType=None):

    width = cell[2] - cell[0]
    height = cell[3] - cell[1]
    if(width <= 2 or height <= 2):
        for y in range(cell[1], cell[3]):
            for x in range(cell[0], cell[2]):
                outputImage.putpixel(xy=(x, y), value=inputPixels[x, y])
        return

    avgColor = avg(pixels=inputPixels, cell=cell)
    deviation = sumOfSquares(pixels=inputPixels, cell=cell, avgPixel=avgColor)

    if(deviation <= thresh):
        for y in range(cell[1], cell[3]):
            for x in range(cell[0], cell[2]):
                if(showEdges and (x==cell[0] or y==cell[1] or x==cell[2]-1 or y==cell[3]-1)):
                    edgeColor = (0, 0, 0)
                    if(edgeType == 'inv'):
                        edgeColor = inv(avgColor)
                    if(edgeType == 'black'):
                        edgeColor = (0, 0, 0)
                    if(edgeType == 'white'):
                        edgeColor = (255, 255, 255)
                    outputImage.putpixel(xy=(x, y), value=edgeColor)
                else:    
                    outputImage.putpixel(xy=(x, y), value=avgColor)
        return
    
        
    halfWidth = math.floor(width / 2)
    halfHeight = math.floor(height / 2)
    cell0 = [ cell[0], cell[1], cell[0] + halfWidth, cell[1] + halfHeight]
    cell1 = [ cell[0] + halfWidth, cell[1], cell[2], cell[1] + halfHeight]
    cell2 = [ cell[0], cell[1] + halfHeight, cell[0] + halfWidth, cell[3]]
    cell3 = [ cell[0] + halfWidth, cell[1] + halfHeight, cell[2], cell[3]]

    quantize(cell0, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, showEdges=showEdges, edgeType=edgeType)
    quantize(cell1, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, showEdges=showEdges, edgeType=edgeType)
    quantize(cell2, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, showEdges=showEdges, edgeType=edgeType)
    quantize(cell3, inputPixels=inputPixels, outputImage=outputImage, thresh=thresh, showEdges=showEdges, edgeType=edgeType)


