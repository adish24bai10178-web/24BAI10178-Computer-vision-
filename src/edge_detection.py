import cv2


def detect_edges(gray_image):

    edges = cv2.Canny(
        gray_image,
        100,
        200
    )

    return edges
