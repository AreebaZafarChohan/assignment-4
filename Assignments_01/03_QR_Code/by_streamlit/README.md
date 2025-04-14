# QR Code Generator & Scanner

A simple and interactive **QR Code Generator & Scanner** built using [Streamlit](https://streamlit.io/), [qrcode](https://pypi.org/project/qrcode/), [OpenCV](https://opencv.org/), and [Pillow](https://pillow.readthedocs.io/). This application allows users to generate QR codes in various formats (PNG, SVG, JPEG, PDF) from any URL or text data, and scan uploaded QR code images to extract the embedded data.

## Live Demo:
Check out the live demo of the app [here](https://qr-generator-and-scanner-by-areeba-zafar.streamlit.app/).


## Features

- **QR Code Generation:**  
  - Generate QR codes using custom data (e.g., URLs, text).
  - Support for multiple formats including PNG, SVG, JPEG, and PDF.
  - Customizable design options (fill color, background color).

- **QR Code Scanning:**  
  - Scan and decode QR code images using OpenCV’s QR code detector.
  - Accepts multiple image formats including PNG, JPEG, SVG, and PDF.
  
- **User Interface:**  
  - Interactive UI built with Streamlit.
  - Intuitive file uploader and display options.
  
- **Feedback & Rating:**  
  - Sidebar for submitting user feedback with ratings.
  - Display of feedback history with an option to clear it.

## Prerequisites

Before running the application, make sure you have installed the required Python libraries. You can install them via pip:

```bash
pip install streamlit qrcode[pil] opencv-python-headless pillow numpy
```

## Usage

### Run the App:
```bash
streamlit run your_app_file.py

```

## Generate QR Code:
Enter your URL or text in the input field.

View and download the QR Code in PNG, SVG, JPEG, or PDF formats.

## Scan QR Code:
Upload a QR code image.

The app decodes and displays the embedded data.

## Feedback:
Use the sidebar to submit feedback and rate the app.

## Overview:
- **QR Generation:** Uses `qrcode` to create codes with customizable colors.
- **QR Scanning:** Uses OpenCV to decode QR codes from uploaded images.
- **User Interface:** Built with Streamlit for an interactive experience.

---

Developed with ❤️ by **Areeba Zafar***