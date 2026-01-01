import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.filters import median
from skimage.morphology import disk
from image_utils import load_image, edge_detection

def main():
    image_path = 'my_image.jpg' 

    try:
        original_image = load_image(image_path)
        print("Image loaded successfully.")
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # --- תיקון לשלב ניקוי הרעשים (עובד בכל הגרסאות) ---
    # במקום להשתמש ב-channel_axis, אנחנו יוצרים תמונה ריקה
    # ומנקים כל ערוץ צבע (R, G, B) בנפרד בתוך לולאה.
    clean_image = np.zeros_like(original_image)
    for i in range(3):
        clean_image[:, :, i] = median(original_image[:, :, i], footprint=disk(3))

    # המשך הקוד כרגיל...
    edge_mag = edge_detection(clean_image)

    threshold = 40
    edge_binary = edge_mag > threshold

    # המרה למספרים לשמירה (0 ו-255)
    binary_for_save = (edge_binary * 255).astype(np.uint8)
    
    edge_image = Image.fromarray(binary_for_save)
    edge_image.save('my_edges.png')
    print("Edge image saved as 'my_edges.png'")

    # הצגה בגרף
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(edge_binary, cmap='gray')
    plt.title(f"Edges (Threshold: {threshold})")
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
