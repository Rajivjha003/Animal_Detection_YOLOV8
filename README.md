# Animal Detection with Custom Trained YOLOv8

![Python](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat-square&logo=python)
![Ultralytics](https://img.shields.io/badge/Ultralytics-8.1.29-green.svg?style=flat-square)

## Overview

Welcome to the Animal Detection with Custom Trained YOLOv5 project! This application enables real-time animal detection using a custom-trained YOLOv5 model integrated with OpenCV. Whether you're monitoring wildlife or studying animal behavior, this tool provides accurate and efficient detection capabilities.

### Key Features

- Real-time animal detection using the webcam feed.
- Support for multiple animal species with customizable class labels.
- Integration with OpenCV for seamless execution and visualization.
- Efficient inference leveraging hardware acceleration platforms.

## Installation

To run the Animal Detection with Custom Trained YOLOv5 project, follow these steps:

1. Clone this repository to your local machine.
2. Install Python 3.9 and create a virtual environment.
3. Install required dependencies: `pip install -r requirements.txt`.
4. Download the YOLOv8 model weights and place them in the specified directory.
5. Run the `main.py` script.

## Folder Structure

```
📂 animal_detection_yolov5/
├── 📁 data/
│   ├── 📁 train/
│   │   ├── 📁 images/
│   │   └── 📁 labels/
│   └── 📁 valid/
│       ├── 📁 images/
│       └── 📁 labels/
├── 📂 runs/
│   └── 📂 detect/
│       └── 📂 train/
│           └── 📂 weights/
│               └── 📄 best.pt
├── 📄 main.py
├── 📄 config.yaml
├── 📄 model.py
└── 📄 requirements.txt
```

## Usage

```bash
python main.py
```

## Screenshots

![Screenshot 1](https://raw.githubusercontent.com/example/animal-detection/main/screenshot1.jpg)
![Screenshot 2](https://raw.githubusercontent.com/example/animal-detection/main/screenshot2.jpg)

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README includes a folder structure section formatted using emojis and modern design elements for a trendy and professional look. Adjust the structure and emojis as needed to match your project's layout and preferences.