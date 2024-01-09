import cv2
import numpy as np

# Function to get the dominant color using k-means clustering
def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, flags)

    # Using numpy.unique to get unique values and their frequencies
    unique_labels, label_counts = np.unique(labels, return_counts=True)

    # Finding the label with the maximum count
    dominant_label = unique_labels[np.argmax(label_counts)]

    # Finding the centroid corresponding to the dominant label
    dominant_color = centroids[dominant_label]

    return np.uint8(dominant_color)

# Variable to track mouse click
clicked = False

# Mouse event handler
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

# Open the camera
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('camera')
cv2.setMouseCallback('camera', onMouse)

# Read the first frame
success, frame = cameraCapture.read()

# Main loop to capture video until a mouse click occurs
while success and not clicked:
    cv2.waitKey(1)
    success, frame = cameraCapture.read()

    # Convert the frame to grayscale and apply median blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)

    # Detect circles using HoughCircles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=40)

    if circles is not None:
        # Convert to integer
        circles = np.uint16(np.around(circles))
        max_r, max_i = 0, 0

        # Find the largest circle
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]

        x, y, r = circles[:, :, :][0][max_i]

        # Check if the circle is within the frame boundaries
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]
            dominant_color = get_dominant_color(square, 2)

            if dominant_color[2] > 100:
                print("STOP")
            elif dominant_color[0] > 80:
                print("Color: ", dominant_color)

                # Extract color information from three zones within the circle
                zone_0 = square[square.shape[0]*3//8:square.shape[0]*5//8, square.shape[1]*1//8:square.shape[1]*3//8]
                zone_0_color = get_dominant_color(zone_0, 1)
                print("Zone 0 Color: ", zone_0_color)

                zone_1 = square[square.shape[0]*1//8:square.shape[0]*3//8, square.shape[1]*3//8:square.shape[1]*5//8]
                zone_1_color = get_dominant_color(zone_1, 1)
                print("Zone 1 Color: ", zone_1_color)

                zone_2 = square[square.shape[0]*3//8:square.shape[0]*5//8, square.shape[1]*5//8:square.shape[1]*7//8]
                zone_2_color = get_dominant_color(zone_2, 1)
                print("Zone 2 Color: ", zone_2_color)

                # Decision logic based on color information
                if zone_1_color[2] < 60:
                    if sum(zone_0_color) > sum(zone_2_color):
                        print("LEFT")
                    else:
                        print("RIGHT")
                else:
                    if sum(zone_1_color) > sum(zone_0_color) and sum(zone_1_color) > sum(zone_2_color):
                        print("FORWARD")
                    elif sum(zone_0_color) > sum(zone_2_color):
                        print("FORWARD AND LEFT")
                    else:
                        print("FORWARD AND RIGHT")
            else:
                print("N/A")

        # Draw circles on the original frame
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Display the frame
    cv2.imshow('camera', frame)

# Release the camera and close windows
cv2.destroyAllWindows()
cameraCapture.release()
