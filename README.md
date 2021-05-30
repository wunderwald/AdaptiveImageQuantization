# AdaptiveImageQuantization

## Usage

Call quantize with the following params:

- cell: a square that defines the region that will be quantized (x0, y0, x1, y1)
- inputPixels: a 2d array of rgb-tuples
- outputImage: a PIL image with dims = cell
- thresh: the threshold for sum-of-squares deviations inside of cells
- minCellDims: array where 0: minWidth, 1: minHeight. Smaller cells are ignored (default: 2, 2)
- showEdges: bool, indicates wether cell edges are drawn
- edgeType: if showEdges==true, determines the type of edges. Options: 'black' (default), 'white', 'inv', 'darken', 'lighten')

## Demo

### Raw

!["Demo Image (raw)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/inputDemo.jpg)

### Quantized (edgeType='inv', thresh=6900, minCellDims=[6, 6])

!["Demo Image (quantized)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/demoOut/out_6900_inv_min6x6.png)


### Quantized (edgeType='white', thresh=42000, minCellDims=[6, 6])

!["Demo Image (quantized)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/demoOut/out_42000_white_min6x6.png)

### Quantized (edgeType='inv', thresh=6900, minCellDims=[4, 4], secret tripp mode)

!["Demo Image (quantized)"](https://github.com/wunderwald/AdaptiveImageQuantization/blob/master/demoOut/tripp_6900_inv_min4x4.png)
