import numpy as np

class Algorithm:
    def process_frame(self, frame: np.ndarray) -> float:
        """
        Processes a frame using the algorithm.

        Args:
            frame (numpy.ndarray): The current frame to be processed.

        Returns:
            (float) the angle AgroBot should move, in the range [-90, 90].
        """
        raise NotImplementedError