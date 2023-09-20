# Fruits Classification with TensorFlow and EfficientNet

![Screenshot 2023-09-21 at 12 51 14 AM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/f25b53ed-34cf-424c-be52-b96fe153773f)

This repository contains code for training a fruit classification model using TensorFlow and the Resnet architecture. The model is trained on a dataset of images and can classify them into 131 different classes.

## Introduction

Fruit classification is a common image classification task. This codebase demonstrates the process of training a fruit classification model using the ResNet architecture, emphasizing accuracy as a key evaluation metric.

## Getting Started

Before running the code, ensure you have the following dependencies installed:
- TensorFlow 2.0
- NumPy
- Matplotlib
- Scikit-Learn

## Data Preparation
Place your training images of fruits in the /Training directory or update the train_path variable in the code to the correct path.

Organize your training data into subdirectories, where each subdirectory corresponds to a different fruit class.

## Data Augmentation
Data augmentation techniques are applied to increase the diversity of training data. Augmentation methods such as random flips, rotations, and color adjustments are used to enhance the model's ability to generalize.

## Model Architecture
The code uses the ResNet architecture as the backbone for the fruit classification model. The architecture is tailored to the specific number of fruit classes and adjusted as needed.

## Training
Training is performed in two stages:

 - The entire model is trained for one epoch to fine-tune the final classification layer while keeping the backbone frozen.

 - After the first stage, the backbone layers are unfrozen, and the entire model is further trained for multiple epochs.
## Callbacks
Important callbacks, such as ModelCheckpoint and EarlyStopping, are used during training to save the best model weights based on validation performance and stop training if the validation loss does not improve.

## Results
The training history and evaluation metrics, including accuracy, are logged during training. These metrics provide insights into the model's classification performance.

## Usage
To train the fruit classification model, execute the code in your preferred Python environment. Ensure that you update the paths and hyperparameters according to your dataset and requirements.


  
