from PIL import Image
import numpy as np

def get_brightness_matrix(pixel_matrix):
    return [0.21*r + 0.72*g + 0.07*b for row in pixel_matrix for (r,g,b) in row]

def main():
    img=Image.open("geto.jpeg")
    px_arr = np.array(img)

    brightness_matrix = get_brightness_matrix(px_arr)
    print(brightness_matrix)

if __name__ == "__main__":
    main()
