import cv2
import os


def detect_faces(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    cascade_path = os.path.join(
        "models",
        "haarcascade_frontalface_default.xml"
    )

    if not os.path.exists(cascade_path):
        raise FileNotFoundError(
            "Haar Cascade model not found at: "
            + cascade_path
        )

    face_cascade = cv2.CascadeClassifier(
        cascade_path
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    result = image.copy()

    for (x, y, w, h) in faces:

        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            result,
            "Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    return result, len(faces)
