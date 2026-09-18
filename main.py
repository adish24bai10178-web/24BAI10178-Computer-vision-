import argparse
import os
import sys
import cv2

from src.preprocessing import preprocess_image
from src.edge_detection import detect_edges
from src.face_detection import detect_faces
from src.image_analysis import analyze_image


def print_header():
    print("=" * 55)
    print("       COMPUTER VISION IMAGE ANALYZER")
    print("=" * 55)


def main():

    parser = argparse.ArgumentParser(
        description="CLI-based Computer Vision Image Analysis System"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input image"
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Directory for generated output images"
    )

    args = parser.parse_args()

    print_header()

    if not os.path.isfile(args.input):
        print(f"\nERROR: Input image not found: {args.input}")
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)

    print("\n[1/5] Loading image...")

    image = cv2.imread(args.input)

    if image is None:
        print("ERROR: OpenCV could not read the image.")
        sys.exit(1)

    print("      ✓ Image loaded successfully")


    print("\n[2/5] Preprocessing image...")

    gray, resized = preprocess_image(image)

    cv2.imwrite(
        os.path.join(args.output, "grayscale.jpg"),
        gray
    )

    cv2.imwrite(
        os.path.join(args.output, "resized.jpg"),
        resized
    )

    print("      ✓ Grayscale conversion completed")
    print("      ✓ Image resized to 600x400")

    print("\n[3/5] Detecting edges...")

    edges = detect_edges(gray)

    cv2.imwrite(
        os.path.join(args.output, "edges.jpg"),
        edges
    )

    print("      ✓ Canny edge detection completed")

    
    print("\n[4/5] Detecting faces...")

    face_image, face_count = detect_faces(image)

    cv2.imwrite(
        os.path.join(args.output, "face_detection.jpg"),
        face_image
    )

    print(f"      ✓ {face_count} face(s) detected")


    print("\n[5/5] Analyzing image...")

    analysis = analyze_image(image)

    print(f"      ✓ Width: {analysis['width']} pixels")
    print(f"      ✓ Height: {analysis['height']} pixels")
    print(f"      ✓ Channels: {analysis['channels']}")
    print(f"      ✓ Total pixels: {analysis['total_pixels']}")
    print(f"      ✓ Image size: {analysis['image_size_kb']:.2f} KB")

    print("\n" + "=" * 55)
    print("       PROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 55)

    print("\nOutput files:")

    print(
        f"  → {os.path.join(args.output, 'grayscale.jpg')}"
    )

    print(
        f"  → {os.path.join(args.output, 'resized.jpg')}"
    )

    print(
        f"  → {os.path.join(args.output, 'edges.jpg')}"
    )

    print(
        f"  → {os.path.join(args.output, 'face_detection.jpg')}"
    )


if __name__ == "__main__":
    main()
