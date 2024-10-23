import numpy as np

class Algorithm:
    ## TODO: When I figure out what datatype lidar is update its type here
    def process_frame(self, frame: np.ndarray, lidar: any) -> float:
        """
        Processes a frame using the algorithm.

        Args:
            frame (numpy.ndarray): The current frame to be processed.
            lidar (any): Current frame of lidar data

        Returns:
            (float) the angle AgroBot should move, in the range [-90, 90].
        """
        raise NotImplementedError