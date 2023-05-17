# Moving Object Detection using OpenCV

This code implements a simple motion detection algorithm using OpenCV (Open Source Computer Vision Library). It captures frames from a video camera, compares them with the first frame, and detects any significant changes in the scene. If a moving object is detected, it is outlined with a green rectangle, and the text "Moving object detected" is displayed on the screen.

## Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- Imutils (`imutils`)

## Installation
1. Make sure you have Python installed on your system. You can download it from the official website: https://www.python.org/downloads/
2. Install the required dependencies by running the following command:
   ```
   pip install opencv-python numpy imutils
   ```

## Usage
1. Connect a video camera to your computer.
2. Run the script using the following command:
   ```
   python motion_detection.py
   ```
3. The camera feed window will open, showing the live video stream.
4. If a moving object is detected, it will be outlined with a green rectangle, and the text "Moving object detected" will be displayed.
5. Press the 'q' key to quit the program.

## Code Explanation
- The code starts by importing the necessary libraries: `cv2` for OpenCV, `numpy` for numerical operations, `time` for delaying execution, and `imutils` for image processing utilities.
- It initializes the video capture by creating a `VideoCapture` object (`cam`) and waits for 1 second to allow the camera to stabilize.
- The variable `firstFrame` is used to store the first frame captured from the camera. This frame is used as a reference for comparison with subsequent frames.
- The `area` variable defines the minimum contour area required to consider an object as significant. Adjust this value according to your needs.
- The code enters an infinite loop to continuously process video frames from the camera.
- Within each iteration of the loop:
  - The code reads a frame from the camera using `cam.read()` and assigns it to the `img` variable.
  - The text variable is set to "Normal" by default, indicating no moving object detected in the current frame.
  - The captured frame is resized to a width of 500 pixels using `imutils.resize()`.
  - The frame is converted to grayscale and then blurred using Gaussian smoothing.
  - If it's the first frame, it is stored in `firstFrame`, and the loop continues to the next iteration.
  - The absolute difference between the current frame and `firstFrame` is calculated using `cv.absdiff()`.
  - A binary threshold image is obtained by applying a threshold to the difference image using `cv.threshold()`.
  - The thresholded image is dilated to reduce noise using `cv.dilate()`.
  - Contours are detected in the thresholded image using `cv.findContours()`.
  - The `grab_contours()` function from `imutils` is used to extract the actual contours from the result of `cv.findContours()`.
  - For each contour, if its area is smaller than the specified `area`, it is ignored.
  - The bounding rectangle of significant contours is drawn on the original frame using `cv.rectangle()`.
  - The `text` variable is updated to "Moving object detected" if at least one significant contour is found.
  - The text is displayed on the frame using `cv.putText()`.
  - The processed frame is displayed in a window named "CameraFeed" using `cv.imshow()`.
  - The loop continues until the 'q' key is pressed, which is checked using `cv.waitKey()`.
- Once

 the loop is terminated, the video capture is released using `cam.release()` and all OpenCV windows are closed using `cv.destroyAllWindows()`.

Feel free to customize the code according to your specific requirements or integrate it into your own projects.
