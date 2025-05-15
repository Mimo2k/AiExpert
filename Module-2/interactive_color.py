import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Remove green
        filtered_image[:, :, 0] = 0  # Remove blue
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Remove green
        filtered_image[:, :, 2] = 0  # Remove red
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Remove blue
        filtered_image[:, :, 2] = 0  # Remove red
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    
    return filtered_image

# Load image
image_path = 'Module-2\image.jpg'  # Change this to your image path
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found at", image_path)
    exit()

print("📷 Image loaded successfully!")
print("\n🎨 Press a key to apply filters:")
print("  r - Red Tint")
print("  b - Blue Tint")
print("  g - Green Tint")
print("  i - Increase Red Intensity")
print("  d - Decrease Blue Intensity")
print("  o - Original Image")
print("  q - Quit")

# Key to filter mapping
key_to_filter = {
    ord('r'): 'red_tint',
    ord('b'): 'blue_tint',
    ord('g'): 'green_tint',
    ord('i'): 'increase_red',
    ord('d'): 'decrease_blue',
    ord('o'): 'original',
}

# Default filter
filter_type = 'original'

while True:
    # Apply the filter
    if filter_type == 'original':
        filtered_image = image.copy()
    else:
        filtered_image = apply_color_filter(image, filter_type)

    # Display the image
    cv2.imshow("Filtered Image", filtered_image)

    # Wait for a key press
    key = cv2.waitKey(0) & 0xFF

    if key == ord('q'):
        print("👋 Exiting...")
        break
    elif key in key_to_filter:
        filter_type = key_to_filter[key]
    else:
        print("⚠️ Invalid key! Try again.")

# Close all windows
cv2.destroyAllWindows()
