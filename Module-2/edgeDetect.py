import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# Utility function to display images using Matplotlib.
# - Supports both grayscale and color images.
# - Converts BGR images to RGB for correct color display.
# --------------------------------------------------------------
def display_image(image, title="Image"):
    plt.figure(figsize=(8, 6))
    
    # Check if image is grayscale or color
    if len(image.shape) == 2:  # Grayscale
        plt.imshow(image, cmap='gray')
    else:  # Color (BGR to RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
    
    plt.title(title)
    plt.axis('off')
    plt.show()


# --------------------------------------------------------------
# Main interactive function for edge detection and smoothing.
# - Loads image, converts to grayscale.
# - Offers a menu for Sobel, Canny, Laplacian, Gaussian, Median, Exit.
# - Loops until user exits.
# --------------------------------------------------------------
def interactive_edge_detection(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from path '{image_path}'")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image(gray, "Original Grayscale Image")

    while True:
        print("\nChoose an operation:")
        print("a) Sobel Edge Detection")
        print("b) Canny Edge Detection")
        print("c) Laplacian Edge Detection")
        print("d) Gaussian Smoothing")
        print("e) Median Filtering")
        print("f) Exit")

        choice = input("Enter your choice (a-f): ").strip().lower()

        if choice == 'a':
            # Sobel Edge Detection
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            abs_sobelx = cv2.convertScaleAbs(sobelx)
            abs_sobely = cv2.convertScaleAbs(sobely)
            sobel_combined = cv2.bitwise_or(abs_sobelx, abs_sobely)
            display_image(sobel_combined, "Sobel Edge Detection")

        elif choice == 'b':
            # Canny Edge Detection
            try:
                low_thresh = int(input("Enter lower threshold (e.g. 50): "))
                high_thresh = int(input("Enter upper threshold (e.g. 150): "))
                if low_thresh < 0 or high_thresh < 0 or high_thresh <= low_thresh:
                    print("Invalid thresholds. Make sure 0 <= low < high.")
                    continue
            except ValueError:
                print("Please enter valid integer values for thresholds.")
                continue

            edges = cv2.Canny(gray, low_thresh, high_thresh)
            display_image(edges, "Canny Edge Detection")

        elif choice == 'c':
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray, cv2.CV_64F)
            abs_laplacian = cv2.convertScaleAbs(laplacian)
            display_image(abs_laplacian, "Laplacian Edge Detection")

        elif choice == 'd':
            # Gaussian Smoothing
            try:
                ksize = int(input("Enter odd kernel size for Gaussian blur (e.g. 5): "))
                if ksize % 2 == 0 or ksize < 1:
                    print("Kernel size must be a positive odd integer.")
                    continue
            except ValueError:
                print("Please enter a valid integer for kernel size.")
                continue
            
            smoothed = cv2.GaussianBlur(gray, (ksize, ksize), 0)
            display_image(smoothed, f"Gaussian Smoothing (Kernel Size: {ksize})")

        elif choice == 'e':
            # Median Filtering
            try:
                ksize = int(input("Enter odd kernel size for Median filter (e.g. 5): "))
                if ksize % 2 == 0 or ksize < 1:
                    print("Kernel size must be a positive odd integer.")
                    continue
            except ValueError:
                print("Please enter a valid integer for kernel size.")
                continue

            median_filtered = cv2.medianBlur(gray, ksize)
            display_image(median_filtered, f"Median Filtering (Kernel Size: {ksize})")

        elif choice == 'f':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice, please select from options a-f.")


# --------------------------------------------------------------
# Run the interactive edge detection function with the image path.
# --------------------------------------------------------------
if __name__ == "__main__":
    img_path = "Module-2\image.jpg"  # <-- change this to your image path
    interactive_edge_detection(img_path)
