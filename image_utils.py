from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    pass # Replace the `pass` with your code

def edge_detection(image):
    pass # Replace the `pass` with your code

from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    img = Image.open(path)
    gray_img = img.convert('L')
    return np.array(gray_img)

def edge_detection(image):
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])
    edges = convolve2d(image, kernel, mode='same', boundary='symm')
    return np.abs(edges)
