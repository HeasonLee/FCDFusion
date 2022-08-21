# FCDFusion
A fast and color-reserved fusion method for visible and infrared image pairs, and a metric called color deviation.
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

## Fuse image pairs
1. Put visible image and corresponding infrared image into "/input/visible" and "/input/infrared", respectively. The two .jpg input images should in the same shape and has the same name like "xxx.jpg". You can change codes in "fuse.py" to change the available image type.
1. Run the fusion methods: `python fuse.py`
2. Fusion results of RGB, YIQ, HSV and FCDFusion methods will be saved in "/output/<method name>".
