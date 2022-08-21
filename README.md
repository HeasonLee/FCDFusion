# FCDFusion
A fast and color-preserving fusion method for visible and infrared image pairs, and a metric called color deviation.
This is the Python implementation of the paper "FCDFusion: A fast fusion method for visible and infrared image pairs with little color deviation".
When the paper is available in Computational Visual Media 2023, a link will be provided here.

# Environment
numpy

opencv-python
- These codes run in Python environment on the CPU to show the algorithms. If you need speed up, please rewrite them in C language or use CUDA and other GPU accelerators.

# How to use
Download or clone the repository:

`git clone https://github.com/HeasonLee/FCDFusion`

Go into the directory "/FCDFusion":

`cd FCDFusion`

## Fuse image pairs using RGB, YIQ, HSV and FCDFusion methods
1. Put visible images and corresponding infrared images into "/input/visible" and "/input/infrared", respectively. The two paired input images should be in the same shape and has the same name like "xxx.jpg". You can change codes in "fuse.py" to change the available image type.
2. Run the fusion methods: `python fuse.py`
3. Fusion results of RGB, YIQ, HSV and FCDFusion methods will be saved in "/output/<method name>".

- 6 pairs of test images are already in "/input/visible" and "/input/infrared". You can find more test image pairs in VIFB or other datasets.

## Compute color deviation metric of fused images
1. Put visible images and corresponding fused images into "/input/visible" and "/output/<method name>", respectively. The two paired images should be in the same shape and has the same name like "xxx.jpg". You can change codes in "color_deviation.py" to change the available image type.
2. Run the script: `python color_deviation.py`
3. Color deviation of each fused image and the average value will be shown in the screen and saved in "/output/color_deviation_values.txt".

- Color deviation is the proposed metric that measures color-preserving ability of a fusion method. You can find more metrics in VIFB.
