import math

import numpy as np
import cv2

def Representational(r, g, b):
    return 0.299 * r + 0.287 * g + 0.114 * b

def calculate(img):
    b, g, r = cv2.split(img)
    pixelAt = Representational(r, g, b)
    return pixelAt

def main():
    # load images (orignal image & compressed image)
    orignal_image = cv2.imread("orignal_image.png", 1)
    compressed_image = cv2.imread("compressed_image.png", 1)

    # get image height and width
    height, width = orignal_image.shape[:2]

    orignalPixelAt = calculate(orignal_image)
    compressedPixelAt = calculate(compressed_image)

    diff = orignalPixelAt - compressedPixelAt
    error = np.sum(np.abs(diff) ** 2)

    error = error / (height * width)

    PSNR = -(10 * math.log10(error / (255 * 255)))
    # MSR = error_sum/(height*width)

    print("PSNR value is {}".format(PSNR))

if __name__ == "__main__":
    main()
