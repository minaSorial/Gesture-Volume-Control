# Hand Gesture Volume Control

## Description

This project implements a hand gesture-based volume control system using OpenCV, MediaPipe, and Pycaw. The program detects hand gestures via webcam, calculates the distance between the thumb and index finger, and maps this distance to the system's volume level.

## Features

- Real-time hand tracking using MediaPipe
- Volume control using thumb-index finger distance
- Visual feedback with on-screen indicators
- FPS display for performance monitoring
- Exit the program by pressing 'q'

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- Pycaw
- Comtypes

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/minaSorial/hand-gesture-volume-control.git
   cd hand-gesture-volume-control
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe numpy pycaw comtypes
   ```

## Usage

1. Run the script:
   ```bash
   python src/hand_volume_control.py
   ```
2. Adjust the system volume by moving your thumb and index finger closer or further apart.
3. Press 'q' to exit the program.

## File Structure

```
├── src                    # Source code directory
│   ├── HandTackingModule.py   # Hand tracking module
│   ├── hand_volume_control.py # Main script for volume control
├── resources              # Contains images and videos
│   ├── VolumeGestureControl.mp4 # Demo video
├── README.md              # Project documentation
```

## Demonstration

<video width="600" controls autoplay loop>
  <source src="resources/VolumeGestureControl.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Troubleshooting

- If the volume does not change, ensure your microphone or speaker devices are correctly detected.
- If the hand tracking is inaccurate, adjust the `detection_conf` parameter in `HandTackingModule.py`.

## Author

[Mina Sorial](https://github.com/minaSorial)

## License

This project is licensed under the MIT License.
