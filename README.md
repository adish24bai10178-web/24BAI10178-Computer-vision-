# 24BAI10178-Computer-vision-
A command-line Computer Vision application built with Python and OpenCV for image preprocessing, grayscale conversion, edge detection, face detection, and image analysis.
# Computer Vision Image Analysis System

A command-line based Computer Vision project developed using Python and OpenCV.

The project performs image preprocessing, grayscale conversion, image resizing, Canny edge detection, Haar Cascade face detection, and basic image analysis.

## Features

* Image loading from the command line
* Grayscale conversion
* Image resizing
* Canny edge detection
* Face detection
* Image dimension analysis
* Pixel-count calculation
* Automatic output generation
* Completely terminal-based execution

## Technologies

* Python 3
* OpenCV
* NumPy
* Git
* GitHub

## Project Structure

```text
computer-vision-project/
│
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── edge_detection.py
│   ├── face_detection.py
│   └── image_analysis.py
│
├── models/
│   └── haarcascade_frontalface_default.xml
│
├── input/
│   └── sample.jpg
│
├── output/
│   └── .gitkeep
│
└── docs/
    └── project_report.md
```

## Requirements

* Python 3.8 or later
* pip
* Terminal / Command Prompt / PowerShell

No GUI application is required.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/computer-vision-project.git
```

Enter the project directory:

```bash
cd computer-vision-project
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Model Setup

Place the Haar Cascade model at:

```text
models/haarcascade_frontalface_default.xml
```

The model can be obtained from the OpenCV Haar Cascade repository.

## Running the Project

Place an image inside the `input` folder.

For example:

```text
input/sample.jpg
```

Run:

```bash
python main.py --input input/sample.jpg
```

The project can also accept a custom output directory:

```bash
python main.py --input input/sample.jpg --output output
```

## Example Terminal Output

```text
=======================================================
       COMPUTER VISION IMAGE ANALYZER
=======================================================

[1/5] Loading image...
      ✓ Image loaded successfully

[2/5] Preprocessing image...
      ✓ Grayscale conversion completed
      ✓ Image resized to 600x400

[3/5] Detecting edges...
      ✓ Canny edge detection completed

[4/5] Detecting faces...
      ✓ 2 face(s) detected

[5/5] Analyzing image...
      ✓ Width: 1920 pixels
      ✓ Height: 1080 pixels
      ✓ Channels: 3
      ✓ Total pixels: 2073600
      ✓ Image size: 6075.00 KB

=======================================================
       PROCESSING COMPLETED SUCCESSFULLY
=======================================================

Output files:
  → output/grayscale.jpg
  → output/resized.jpg
  → output/edges.jpg
  → output/face_detection.jpg
```

The exact number of detected faces and image statistics depend on the input image.

## Output

The program generates four files.

### grayscale.jpg

Grayscale version of the original image.

### resized.jpg

Image resized to 600 × 400 pixels.

### edges.jpg

Edges detected using the Canny Edge Detection algorithm.

### face_detection.jpg

Original image with detected faces marked using bounding boxes.

## Computer Vision Techniques

### 1. Grayscale Conversion

Grayscale conversion transforms a multi-channel color image into a single-channel intensity image.

It simplifies subsequent image-processing operations.

### 2. Image Resizing

Image resizing changes the dimensions of the image.

This is useful for standardizing image sizes and reducing computational requirements.

### 3. Canny Edge Detection

Canny Edge Detection identifies significant intensity changes in an image.

It is commonly used to identify boundaries and structural features.

### 4. Haar Cascade Face Detection

The Haar Cascade classifier is used to detect faces in the image.

The detected faces are represented using rectangular bounding boxes.

## Command-Line Requirement

This project is specifically designed to run without a graphical user interface.

The complete workflow is:

```text
Clone Repository
       ↓
Install Python Dependencies
       ↓
Provide Input Image
       ↓
Run main.py
       ↓
Process Image
       ↓
Save Results
```

No GUI setup, Jupyter Notebook, web browser, or IDE is required.

## Error Handling

The program checks whether:

* The input image exists.
* OpenCV can read the image.
* The Haar Cascade model exists.
* The output directory can be created.

If an error occurs, an appropriate message is displayed in the terminal.

## Applications

The concepts demonstrated in this project can be used in:

* Image processing
* Security systems
* Surveillance
* Automated inspection
* Human-computer interaction
* Image analysis
* Computer vision research

## Limitations

The Haar Cascade method may produce false detections or miss faces depending on:

* Lighting
* Image quality
* Face orientation
* Occlusion
* Image resolution

The project performs basic face detection rather than modern deep-learning-based object recognition.

## Future Scope

The project can be extended with:

* YOLO object detection
* Real-time webcam processing
* Object classification
* Face recognition
* Motion detection
* Eye detection
* Smile detection
* Image segmentation
* Deep-learning-based detection
* Batch processing of multiple images

## Author

**Adish Kashliwal**

Computer Vision Project

## License

This project is intended for educational purposes.
