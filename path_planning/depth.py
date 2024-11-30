import pyzed.sl as sl
import cv2
import numpy as np

def main():
    # Initialize the ZED camera
    zed = sl.Camera()

    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.ULTRA  # Use ULTRA depth mode
    init_params.coordinate_units = sl.UNIT.MILLIMETER  # Depth values in millimeters
    init_params.camera_resolution = sl.RESOLUTION.HD720  # Set resolution to HD720 for faster processing

    # Open the camera
    if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
        print("Failed to open ZED camera.")
        return

    print("ZED camera successfully opened. Press 'q' to quit the application.")

    # Create objects to hold the image and depth map
    left_image = sl.Mat()
    depth_image = sl.Mat()
    runtime_params = sl.RuntimeParameters()

    while True:
        # Capture a new frame
        if zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            # Retrieve the left image
            zed.retrieve_image(left_image, sl.VIEW.LEFT)

            # Retrieve the depth map
            zed.retrieve_image(depth_image, sl.VIEW.DEPTH)

            # Convert depth map to OpenCV format
            depth_map_np = depth_image.get_data()
            depth_map_np = np.nan_to_num(depth_map_np)  # Replace NaNs with 0
            depth_map_normalized = cv2.normalize(depth_map_np, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

            # Display the images
            cv2.imshow("Left Image", left_image.get_data())
            cv2.imshow("Depth Map", depth_map_normalized)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Close the camera and cleanup
    zed.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
