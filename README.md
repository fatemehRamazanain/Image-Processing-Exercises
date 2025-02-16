# Image Processing Exercises 🚀

This repository contains various exercises from the **Digital Image Processing** course, implemented using **Python** and **OpenCV**. Each exercise focuses on a different image processing concept and provides hands-on coding experience.

---
## 📌 Exercise 1: Bit Depth Reduction

### 🎯 Objective
In this exercise, we demonstrate how to reduce the bit depth of a grayscale image to **1-bit, 4-bit, and 8-bit** representations.

### ⚙️ Implementation
- The input grayscale image is loaded using OpenCV (`cv2`).
- Pixel values are adjusted to match the desired bit depth.
- The processed images are displayed and saved for comparison.

### 🚀 How to Run the Code
#### **Prerequisites**
Ensure you have **Python 3.x** and the required dependencies installed. You can install OpenCV using:
```bash
pip install opencv-python numpy
```
#### **Run the script**
To execute the bit depth reduction script, use the following command:
```bash
python 01_bit_depth_reduction.py --input image.jpg
```
Replace `image.jpg` with the path to your input image.

### 📁 Output
The script generates images with different bit depths and saves them in the `results/` directory.

---
## 🏗️ Repository Structure
```
Image-Processing-Exercises/
│── 01_bit_depth_reduction.py  # First exercise script
│── results/                   # Output images from exercises
│── README.md                  # Documentation
│── image.jpg                   # Sample input image
└── requirements.txt            # Dependencies (if needed)
```

---
## 📢 Contributing
Feel free to contribute by adding more exercises or improving the existing ones! 🎉

### 🔗 References
- [OpenCV Documentation](https://docs.opencv.org/)
- [Digital Image Processing Concepts](https://en.wikipedia.org/wiki/Digital_image_processing)

