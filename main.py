#! /usr/bin/env python3

from PIL import Image
import numpy as np

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_brightness_matrix(pixel_matrix):
    brightness_matrix = np.zeros((pixel_matrix.shape[0], pixel_matrix.shape[1]))
    for i in range(len(pixel_matrix)):
        for j in range(len(pixel_matrix[i])):
            r, g, b = pixel_matrix[i][j]
            brightness_matrix[i][j] = 0.21*r + 0.72*g + 0.07*b
    return brightness_matrix

def main():
    img=Image.open("geto.jpeg")

    px_arr = np.array(img)

    brightness_matrix = get_brightness_matrix(px_arr)
    print(brightness_matrix)

if __name__ == "__main__":
    main()
