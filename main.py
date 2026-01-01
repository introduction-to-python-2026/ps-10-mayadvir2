import matplotlib.pyplot as plt
from image_utils import load_image, edge_detection

image_path = 'my_image.jpg' 

try:
    original_image = load_image(image_path)
    edges_image = edge_detection(original_image)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original (Grayscale)")
    plt.imshow(original_image, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title("Edges Detected")
    plt.imshow(edges_image, cmap='gray') 
    plt.axis('off')
    plt.show()
    print("Process completed successfully!")

except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found. Please add an image to the folder.")
except Exception as e:
    print(f"An error occurred: {e}")
