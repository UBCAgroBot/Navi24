import numpy as np
import cv2

def detect_edges(img):
    """
    Finds edges in green (crops) areas of an image.
    """
    # Convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    
    # Create green mask
    green_low = np.array([35, 40, 40])   
    green_high = np.array([90, 255, 255]) 
    green_mask = cv2.inRange(hsv, green_low, green_high)
    
    # Isolating just the green part of the image
    green_segment = cv2.bitwise_and(img, img, mask=green_mask)
    
    # Edge detection
    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(green_segment, cv2.COLOR_RGB2GRAY)
    
    # Detecting edges using Sobel edge detection
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    edges = np.sqrt(sobelx**2 + sobely**2)
    edges = np.uint8(255 * edges / np.max(edges)) #scale to 0-255
    
    return edges