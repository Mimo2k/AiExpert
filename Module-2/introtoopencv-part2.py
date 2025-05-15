import cv2
import os

# Define image path
image_path = os.path.join('Module-2', 'image.jpg')

# Attempt to load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"❌ Error: Could not load image from '{image_path}'")
else:
    print("✅ Image loaded successfully!")

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("🎨 Converted image to grayscale.")

    # Resize to 224x224
    resized_image = cv2.resize(gray_image, (224, 224))
    print("📐 Resized image to 224x224.")

    # Display the image
    window_name = 'Processed Image'
    cv2.imshow(window_name, resized_image)
    print("👀 Press 'S' to save the image or any other key to exit.")

    # Wait for a key press
    key = cv2.waitKey(0)

    # Check if 'S' or 's' was pressed
    if key == ord('s') or key == ord('S'):
        save_path = 'grayscale_resized_image.jpg'
        cv2.imwrite(save_path, resized_image)
        print(f"💾 Image saved as '{save_path}'")
    else:
        print("⚠️ Image not saved.")

    # Close the display window
    cv2.destroyAllWindows()

    # Print final image properties
    height, width = resized_image.shape
    print(f"📏 Processed Image Dimensions: {width}x{height}")
