# AdaptiveImageQuantization

## Usage (via demo script)
place input image in root directory, call it "input.jpg". Run the script main and the quantization results for a set of different parametrizations will be written to ./out.

## Usage (quantize.py)
Call quantize with the following params:

- cell: a square that defines the region that will be quantized (x0, y0, x1, y1) 
- inputPixels: a 2d array of rgb-tuples
- outputImage: a PIL image with dims = cell
- thresh: the threshold for sum-of-squares deviations inside of cells
- showEdges: bool, indicates wether cell edges are drawn
- edgeType: if showEdges==true, determines the type of edges. Options: 'black' (default), 'white', 'inv' (inverted average color of cell)

## Demo

### Raw
!["Demo Image (raw)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/input.jpg)

### Quantized (edgeType='inv', thresh=690000)
!["Demo Image (quantized)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/out/out_690000_inv.jpg)


### Quantized (edgeType='black', thresh=6900)
!["Demo Image (quantized)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/out/out_6900_black.jpg)
