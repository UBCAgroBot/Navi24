import cv2 as cv
import numpy as np
import math

class Midpoint_Finder:

    def __init__(self):
        # Load the input image
        self.img_path = "C:/Users/USER/Desktop/agrobotsnavi(testing)/path_planning_algorithm/1_fieldcornrow.png"  # Replace with your image path if testing elsewhere
        self.img = cv.imread(self.img_path, cv.IMREAD_COLOR)
        if self.img is None:
            raise FileNotFoundError(f"Image file '{self.img_path}' not found. Check the file path.")

        # HSV thresholds for green
        self.LOW_GREEN_HSV = np.array([35, 40, 40])
        self.HIGH_GREEN_HSV = np.array([85, 255, 255])

    def green_mask(self):
        # Convert image to HSV
        hsv_img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)

        # Create binary mask for green
        green_mask = cv.inRange(hsv_img, self.LOW_GREEN_HSV, self.HIGH_GREEN_HSV)

        # Apply morphological operations to clean the mask
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
        cleaned_image = cv.morphologyEx(green_mask, cv.MORPH_OPEN, kernel)

        # Apply a region of interest (lower portion of the image)
        roi = np.zeros_like(cleaned_image)
        height = cleaned_image.shape[0]
        roi[int(height * 0.6):, :] = 1  # Only keep the bottom 40% of the image
        cleaned_image = cv.bitwise_and(cleaned_image, cleaned_image, mask=roi)

        return cleaned_image
            
    def find_contours(self):
        # Get the green mask
        green_mask = self.green_mask()

        # Find contours in the mask
        contours, _ = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Filter contours to remove noise
        contours = [cnt for cnt in contours if cv.contourArea(cnt) > 500]  # Adjust area threshold if needed

        return contours

    def get_left_right_contours(self, contours):
        # Split contours into left and right based on their position relative to the image center
        img_center_x = self.img.shape[1] // 2
        left_contours = [cnt for cnt in contours if cv.boundingRect(cnt)[0] < img_center_x]
        right_contours = [cnt for cnt in contours if cv.boundingRect(cnt)[0] >= img_center_x]

        # Select the largest contour from each group
        left_contour = max(left_contours, key=cv.contourArea, default=None)
        right_contour = max(right_contours, key=cv.contourArea, default=None)

        return left_contour, right_contour

    def calculate_centroid(self, contour):
        # Calculate the centroid of a contour
        M = cv.moments(contour)
        if M['m00'] == 0:
            return None
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        return (cx, cy)

    def calculate_midpoint(self, left_center, right_center):
        # Calculate the midpoint between the left and right centers
        midpoint = (
            (left_center[0] + right_center[0]) // 2,
            (left_center[1] + right_center[1]) // 2,
        )
        return midpoint

    def annotate_image(self, left_center, right_center, midpoint):
        # Copy the original image for annotation
        annotated_img = self.img.copy()

        # Draw centers
        if left_center:
            cv.circle(annotated_img, left_center, 5, (255, 0, 0), -1)  # Blue for left center
        if right_center:
            cv.circle(annotated_img, right_center, 5, (255, 0, 0), -1)  # Blue for right center
        if midpoint:
            cv.circle(annotated_img, midpoint, 5, (0, 0, 255), -1)  # Red for midpoint

        # Draw lines between the points
        if left_center and right_center:
            cv.line(annotated_img, left_center, right_center, (0, 255, 0), 2)

        return annotated_img
        
if __name__ == "__main__":
    try:
        # Instantiate the Midpoint_Finder class
        finder = Midpoint_Finder()

        # Find contours and split into left and right
        contours = finder.find_contours()
        left_contour, right_contour = finder.get_left_right_contours(contours)

        if left_contour is not None and right_contour is not None:
            # Calculate centroids
            left_center = finder.calculate_centroid(left_contour)
            right_center = finder.calculate_centroid(right_contour)

            # Calculate midpoint
            if left_center and right_center:
                midpoint = finder.calculate_midpoint(left_center, right_center)

                # Annotate and display the final image
                annotated_img = finder.annotate_image(left_center, right_center, midpoint)
                cv.imshow("Annotated Image", annotated_img)
                cv.waitKey(0)
                cv.destroyAllWindows()

    except FileNotFoundError as e:
        print(e)