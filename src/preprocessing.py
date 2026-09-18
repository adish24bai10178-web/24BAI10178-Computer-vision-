import cv2


def preprocess_image(image):

    # Convert BGR image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Resize image
    resized = cv2.resize(
        image,
        (600, 400)
    )

    return gray, resized
