import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_image(path):
    """
    Reads an image from a file path and converts it into a NumPy array.
    """
    img = Image.open(path)
    return np.array(img)

def edge_detection(image_array):
    """
    Performs edge detection on an image array using Sobel-like filters.
    """
    # 1. Convert to grayscale
    grayscale = np.mean(image_array, axis=2)

    # 2. Define Vertical Filter (Kernel Y)
    kernelY = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    # 3. Define Horizontal Filter (Kernel X)
    kernelX = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    # 4. Apply convolutions
    edgeY = convolve2d(grayscale, kernelY, mode='same', boundary='fill', fillvalue=0)
    edgeX = convolve2d(grayscale, kernelX, mode='same', boundary='fill', fillvalue=0)

    # 5. Compute Magnitude
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG
