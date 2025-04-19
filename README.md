## **Face Detection using OpenCV and Deep Learning**

Welcome to my face detection project, where I explore various techniques in computer vision, ranging from classical approaches to advanced deep learning-based methods. This repository showcases my journey in face detection, starting with OpenCV’s traditional Haar Cascades and transitioning to deep learning models.

## Project Overview

In this project, I dive into face detection techniques and experiment with both classical and modern methods. I started with OpenCV’s built-in models like Haar Cascades and later implemented deep learning approaches using Convolutional Neural Networks (CNNs).

## Project Structure

The project is structured into the following categories:
face-detection/
├── haar_cascade/                 # Classical face detection using Haar Cascades
│   ├── haar_face_detect.py      # Detection script
│   └── haar_config.xml          # Haar cascade XML file
├── deep_learning_model/         # Deep learning-based face detection
│   ├── cnn_model.py             # CNN implementation
│   ├── dataset/                 # Dataset used for training/testing
│   └── model_results/           # Saved model or results
├── utils/                       # Utility scripts
│   └── image_processing.py      # Preprocessing, resizing, etc.
├── results/                     # Outputs and demo visuals
│   ├── result1.png
│   ├── result2.png
│   └── accuracy_plot.png
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation

## Project Highlights

This project covers the key aspects of face detection using different approaches:
1. ** Face Detection with Haar Cascade (Classical)
   
 In this section, face detection is implemented using OpenCV’s pre-trained Haar Cascade classifier. This classical method is ideal for quick face detection tasks but has limitations when dealing with complex scenarios or varying face angles.

2. **  Deep Learning-Based Face Detection                                                                     This part uses Convolutional Neural Networks (CNNs) for face detection, offering better accuracy and robustness than traditional methods. The CNN model is trained on large datasets, enabling it to generalize well for real-world applications.

3. ** Simulated CNN Application
   
After learning CNNs, I implemented a model using Simpson’s dataset from Kaggle, aiming to enhance my understanding of feature extraction through kernels and layers in CNNs.

## Key Takeaways 

* Gained in-depth understanding of CNNs, including feature extraction through kernels.
* Achieved an initial accuracy of 50%, with potential for improvement through model fine-tuning.

<img width="1077" alt="face_detection" src="https://github.com/user-attachments/assets/7d533c52-3816-4bfe-aa9e-0a592beefcfe" />

 ![Screenshot 2025-04-19 at 7 21 44 PM](https://github.com/user-attachments/assets/2f84b54f-1e50-459f-8ad9-6f69a584b5c9)
 
 ![Screenshot 2025-04-19 at 7 22 16 PM](https://github.com/user-attachments/assets/5c16f36f-7b33-4772-b44e-ca2dfc171e87)
 
 ![Screenshot 2025-04-19 at 7 22 35 PM](https://github.com/user-attachments/assets/39918c32-0ddd-4ed4-8691-d53096ac063a)





## Features

•	Face detection using OpenCV’s Haar Cascade Classifier (classical approach).
•	Deep learning-based face detection with CNNs.
•	Modular and clean code structure for easy experimentation and extension.
•	Visualizations of model performance and outputs.


## Technologies Used

•	Python: Programming language used for the implementation.
•	OpenCV (cv2): For classical face detection using Haar Cascades.
•	CNN (Convolutional Neural Networks): Deep learning model used for face detection.
•	NumPy: For numerical operations and array manipulation.
•	Matplotlib: For generating visualizations and graphs.

## Installation

To get started with the project, follow these steps:

1. Clone the repository: git clone https://github.com/ShadmanRahman786/Face-Detection.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the project:
   * To test face detection with Haar Cascade, navigate to the haar_cascade directory.
   * For deep learning-based detection, go to the deep_learning_model directory.

## Contribution

Feel free to fork the repository, create a branch, and submit a pull request if you have any improvements or suggestions. Contributions are always welcome!
 
 

