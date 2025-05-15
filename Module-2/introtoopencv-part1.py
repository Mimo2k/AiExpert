import cv2
import os

# Path to the image
image_path = 'Module-2\image.jpg'

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"❌ Error: The file '{image_path}' does not exist.")
else:
    # Load the image
    image = cv2.imread(image_path)

    # Check if image is loaded correctly
    if image is None:
        print(f"❌ Error: Unable to load image '{image_path}'.")
    else:
        # Print image properties
        height, width, channels = image.shape
        print(f"✅ Image Loaded Successfully!")
        print(f"📏 Dimensions: {width}x{height}")
        print(f"🎨 Channels: {channels}")

        # Create a resizable window and resize it (doesn't affect image dimensions)
        window_name = 'Loaded Image'
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 800, 500)

        # Display the image
        cv2.imshow(window_name, image)
        print("🔍 Press any key in the image window to close it.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
