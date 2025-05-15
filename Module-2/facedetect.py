import cv2

# Load Haar Cascade for face detection
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Start webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not access the webcam.")
    exit()

print("🎥 Webcam started. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("⚠️ Error: Unable to read frame from webcam.")
        break

    # Convert frame to grayscale for better detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow("🧠 Face Detection - Press 'q' to Exit", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Quitting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
