# MOSSE Object Tracker

This repository implements a simple **MOSSE (Minimum Output Sum of Squared Error) tracker** using OpenCV and NumPy. The MOSSE tracker is a fast and efficient visual tracking algorithm suitable for real-time applications.

## Features
- 🚀 Real-time object tracking using the MOSSE algorithm
- 🖼️ Select ROI (Region of Interest) to initialize the tracker
- 🔄 Fast detection and adaptive updating of tracking parameters
- 🏗️ Simple OpenCV-based implementation

## Prerequisites
To run this tracker, you need to have the following dependencies installed:

### Required Packages
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

You can install the required dependencies using pip:
```sh
pip install opencv-python numpy
```

## Usage
Run the script to start tracking:
```sh
python mosse_tracker.py
```

### Steps:
1. The script will open your webcam and display the first frame.
2. Select the object to track using your mouse.
3. The tracker will start following the selected object in real time.
4. Press `q` to exit the tracking window.

## How It Works
1. **Initialize the tracker**: The user selects an ROI, which is then preprocessed and used to initialize the MOSSE filter.
2. **Preprocessing**: The selected region is converted to log space and normalized.
3. **Update step**: The filter is updated adaptively based on new frames to improve tracking performance.
4. **Detection step**: The position of the object is estimated using correlation response maps.

## Code Structure
- `MOSSE` class: Implements the MOSSE tracking algorithm.
  - `__init__(frame, rect)`: Initializes the tracker.
  - `preprocess(img)`: Normalizes and filters the input image.
  - `update(frame, rect)`: Updates the tracking filter.
  - `detect(frame)`: Detects the object in the given frame.
- `main()`: Captures video, allows the user to select an object, and continuously tracks it.

## Demo
A short demonstration of the tracker in action:
![MOSSE Tracker](https://upload.wikimedia.org/wikipedia/commons/5/5f/Kalman_filter_tracking.gif)

*Example tracking output*

## License
This project is licensed under the **MIT License**. Feel free to modify and use it as needed.

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests to improve this tracker.

---
Developed with ❤️ using OpenCV & Python.
