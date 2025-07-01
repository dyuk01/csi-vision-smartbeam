import cv2
import numpy as np

def singular(word: str) -> str:
    """
    Convert a word into singular form by removing trailing 's'.

    Parameters:
    word (str): The word to convert.

    Returns:
    str: The singular form of the word.
    """
    return word.lower().rstrip("s")


def calculate_centroid_from_mask(mask: np.ndarray) -> tuple[int, int] | None:
    """
    Calculate the centroid of a binary mask using image moments.

    Parameters:
    mask (np.ndarray): A binary mask where the object is represented by non-zero values.

    Returns:
    tuple[int, int] | None: The (x, y) coordinates of the centroid if the mask exists, otherwise None.
    """
    moments = cv2.moments(mask.astype(np.uint8))
    if moments["m00"] != 0:
        x = int(moments["m10"] / moments["m00"])
        y = int(moments["m01"] / moments["m00"])
        return (x, y)
    return None


def draw_centroid_and_info(frame: np.ndarray, centroid: tuple[int, int], class_name: str, confidence: float, color=(0, 255, 0)) -> None:
    """
    Draw centroid and labels on the frame.

    Parameters:
    frame (np.ndarray): The image frame to draw on.
    centroid (tuple[int, int]): The (x, y) coordinates of the centroid.
    class_name (str): The name of the detected class.
    confidence (float): The confidence score of the detection.
    color (tuple[int, int, int]): The color to use for drawing (default is green).

    Returns:
    None
    """
    if centroid is not None:
        x, y = centroid

        # Draw an empty circle at the centroid to mark the object's center.
        cv2.circle(frame, (x, y), 6, color, -1)

        # Draw a circle outline and crosshair at the centroid.
        cv2.circle(frame, (x, y), 8, (255, 255, 255), 2)
        cv2.line(frame, (x - 15, y), (x + 15, y), color, 2)
        cv2.line(frame, (x, y - 15), (x, y + 15), color, 2)

        # Label the centroid with class name and confidence.
        text = f"{class_name}: ({x}, {y}) conf:{confidence:.2f}"
        
        # Draw a background layer behind the text.
        cv2.putText(frame, text, (x - 50, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Display text.
        cv2.putText(frame, text, (x - 50, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

