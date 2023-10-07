# @Author  : ojas-wani
# @File    : laplacian_filter.py
<<<<<<< HEAD
# @Date    : 10/04/2023

import numpy as np
from cv2 import (
    BORDER_DEFAULT,
    COLOR_BGR2GRAY,
    CV_64F,
    cvtColor,
    filter2D,
    imread,
    imshow,
    waitKey,
)
from digital_image_processing.filters.gaussian_filter import gaussian_filter

def my_laplacian(src: np.ndarray, ksize: int) -> np.ndarray:
    """
    :param src: the source image, which should be a grayscale or color image.
    :param ksize: the size of the kernel used to compute the Laplacian filter,
                  which can be 1, 3, 5 or 7.

    """

    # Create a Laplacian kernel matrix according to the ksize
    if ksize == 1:
        kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    elif ksize == 3:
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    elif ksize == 5:
        kernel = np.array(
            [
                [0, 0, -1, 0, 0],
                [0, -1, -2, -1, 0],
                [-1, -2, 16, -2, -1],
                [0, -1, -2, -1, 0],
                [0, 0, -1, 0, 0],
            ]
        )
    elif ksize == 7:
        kernel = np.array(
            [
                [0, 0, 0, -1, 0, 0, 0],
                [0, 0, -2, -3, -2, 0, 0],
                [0, -2, -7, -10, -7, -2, 0],
                [-1, -3, -10, 68, -10, -3, -1],
                [0, -2, -7, -10, -7, -2, 0],
                [0, 0, -2, -3, -2, 0, 0],
                [0, 0, 0, -1, 0, 0, 0],
            ]
        )

    # Apply the Laplacian kernel using convolution
    laplacian_result = filter2D(
        src, CV_64F, kernel, 0, borderType=BORDER_DEFAULT, anchor=(0, 0)
    )

    return laplacian_result


if __name__ == "__main__":
    # read original image
    img = imread(r"../image_data/lena.jpg")

    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # Applying gaussian filter
    blur_image = gaussian_filter(gray, 3, sigma=1)

    # Apply multiple Kernel to detect edges
    laplacian_image = my_laplacian(ksize=3, src=blur_image)

    imshow("Original image", img)
    imshow("Deteced edges using laplacian filter", laplacian_image)

    waitKey(0)
=======
# @Time    : 10/04/2023

from cv2 import imread, cvtColor, COLOR_BGR2GRAY,  filter2D, imshow, waitKey, CV_64F, BORDER_DEFAULT
from gaussian_filter import gaussian_filter
import numpy as np


def my_laplacian(src, ddepth=-1, ksize=3, scale=1, delta=0, bordertype='default') -> np.ndarray:

  """
  :param src: the source image, which should be a grayscale or color image.
  :param ddepth: the desired depth of the destination image, 
                -1 or one of np.uint8, np.uint16, np.int16, np.float32 or np.float64.
  :param ksize: the size of the kernel used to compute the Laplacian filter, 
                which can be 1, 3, 5 or 7. A larger kernel size will produce more accurate results.
  :param scale: an optional scaling factor applied to the computed Laplacian values, 
                which can be used to enhance or reduce the effect of the filter.
  :param delta: an optional value added to the computed Laplacian values, 
                which can be used to shift the output image intensity range.
  :param bordertype: an optional flag that specifies how to handle the image borders, 
                    which can be one of 'default', 'replicate', 'reflect', or 'constant'.

  """
  
  # Convert the source image to a numpy array
  src = np.array(src)

  # Get the shape and depth of the source image
  src_depth = src.dtype

  # If ddepth is -1, use the same depth as the source image
  if ddepth == -1:
    ddepth = src_depth

  # Create a Laplacian kernel matrix according to the ksize
  if ksize == 1:
    kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
  elif ksize == 3:
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
  elif ksize == 5:
    kernel = np.array([[0, 0, -1, 0 ,0], [0,-1,-2,-1 ,0], [-1,-2 ,16,-2 ,-1], [0,-1,-2,-1 ,0], [0 ,0 ,-1 ,0 ,0]])
  elif ksize == 7:
    kernel = np.array([[0 ,0 ,0 ,-1 ,0 ,0 ,0], [0 ,0 ,-2 ,-3 ,-2 ,0 ,0], [0 ,-2 ,-7 ,-10 ,-7 ,-2 ,0], [-1 ,-3 ,-10 ,68 ,-10 ,-3 ,-1], [0 ,-2 ,-7 ,-10 ,-7 ,-2 ,0], [0 ,0 ,-2 ,-3 ,-2 ,0 ,0], [0 ,0 ,0 ,-1 ,0 ,0 ,0]])

  # Apply the Laplacian kernel using convolution
  laplacian_result = filter2D(src, ddepth, kernel, delta,bordertype=BORDER_DEFAULT, anchor=(0, 0))

  return laplacian_result


if __name__ == "__main__":

  # read original image
  img = imread(r"digital_image_processing/image_data/lena.jpg")

  # turn image in gray scale value
  gray = cvtColor(img,COLOR_BGR2GRAY)

  # Applying gaussian filter
  blur_image = gaussian_filter(gray,3, sigma=1)

  # Apply multiple Kernel to detect edges
  laplacian_image = my_laplacian(blur_image,ddepth=CV_64F, ksize=3)

  imshow("Original image", img)
  imshow("Deteced edges using laplacian filter", laplacian_image)
  
  waitKey(0)
>>>>>>> origin/master
