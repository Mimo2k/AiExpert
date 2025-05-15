import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'Module-2\image.jpg'
image = cv2.imread(image_path)

# Validate image loading
if image is None:
    print(f"❌ Error: Could not load image from '{image_path}'")
else:
    print("✅ Image loaded successfully!")

    # Convert BGR to RGB for correct color display in matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the original RGB image
    plt.figure(figsize=(6, 4))
    plt.imshow(image_rgb)
    plt.title("🌈 Original RGB Image")
    plt.axis('off')
    plt.show()

    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    plt.figure(figsize=(6, 4))
    plt.imshow(gray_image, cmap='gray')
    plt.title("🖤 Grayscale Image")
    plt.axis('off')
    plt.show()

    # Crop a region (e.g., rows 100–300 and columns 200–400)
    h, w = image.shape[:2]
    row_start, row_end = 100, min(300, h)
    col_start, col_end = 200, min(400, w)

    cropped_image = image[row_start:row_end, col_start:col_end]
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

    # Display the cropped region
    plt.figure(figsize=(5, 4))
    plt.imshow(cropped_rgb)
    plt.title(f"✂️ Cropped Region ({row_start}:{row_end}, {col_start}:{col_end})")
    plt.axis('off')
    plt.show()
