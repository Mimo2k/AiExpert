import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Could not load image at '{path}'")
    return img

def rotate_image(image, angle, scale=1.0):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    # Compute rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, scale)
    
    # Calculate the sine and cosine (absolute values)
    abs_cos = abs(M[0, 0])
    abs_sin = abs(M[0, 1])
    
    # Compute new bounding dimensions to avoid clipping
    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)
    
    # Adjust rotation matrix to take into account translation
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]
    
    # Perform the rotation
    rotated = cv2.warpAffine(image, M, (new_w, new_h))
    return rotated

def adjust_brightness(image, value):
    # Create a brightness matrix of the same shape, filled with the brightness value
    brightness_matrix = np.full(image.shape, value, dtype=np.uint8)
    # Add brightness safely
    brighter = cv2.add(image, brightness_matrix)
    return brighter

def show_image(img, title):
    # Convert BGR to RGB for matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(7, 5))
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    image_path = 'Module-2\image.jpg'
    try:
        image = load_image(image_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    show_image(image, "Original Image")
    
    # Rotate by 45 degrees (change angle here)
    rotated_img = rotate_image(image, angle=45)
    show_image(rotated_img, "Rotated Image (45°)")
    
    # Increase brightness by 50 (change brightness value here)
    brighter_img = adjust_brightness(image, value=50)
    show_image(brighter_img, "Brighter Image (+50 brightness)")

if __name__ == "__main__":
    main()
