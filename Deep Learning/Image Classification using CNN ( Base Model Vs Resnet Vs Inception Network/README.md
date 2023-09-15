# Image Classification using Convolutional Neural Networks (CNN) & Transfer Learning Methods such as RESNET & INCEPTION

![Screenshot 2023-09-14 at 11 02 35 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/02217ef1-138b-4fe0-8bd3-5d56f1e17302)

This project focuses on image classification, aiming to distinguish between images of dogs and cats using deep learning techniques. It covers the training of a base CNN model from scratch and later explores transfer learning with pre-trained models, specifically ResNet50V2 and InceptionV3. The final section provides a comparative analysis of these models.

## Table of Contents

### 1 - Setting up the Environment
### 2 - Data Preparation
### 3 - Extracting file paths
### 4 - Removing low-quality images
### 5 - Label encoding
### 6 - Train-test split
### 7 - Data augmentation
### 8 - Creating the Model
### 9 - Defining the CNN architecture
### 10 - Model Training
### 11 - Training the model
### 12 - Transfer Learning
### 13 - Fine-tuning a pre-trained model (ResNet50V2 and InceptionV3)
### 14 - Model Comparison
### 15 - Conclusion
### 16 - Tools Used

## Setting up the Environment

This section includes importing necessary libraries, such as TensorFlow, Keras, and other utility libraries for data manipulation and visualization.

## Data Preparation

I took the dataset from Kaggle. Here's the link https://www.kaggle.com/c/dogs-vs-cats

## Extracting File Paths

my_path: The directory where the training images are stored.
all_paths: List of all image file paths in the training directory.

## Removing Low-Quality Images

A function TestImageQuality is defined to filter out low-quality images. It reads each image file, checks if it's a valid JPEG image, and appends the paths of valid images to paths.

## Label Encoding

The labels for the images (either "Cat" or "Dog") are extracted from file paths and encoded using a label encoder, where "Cat" is mapped to 0 and "Dog" to 1.

## Train-Test Split

The data is split into training and validation sets using train_test_split from scikit-learn.

## Creating TensorFlow Datasets

Two TensorFlow datasets (train_dataset and val_dataset) are created to efficiently load and preprocess images for training and validation. Data augmentation is applied to the training dataset to improve model generalization.

## Creating the Model

![Screenshot 2023-09-14 at 10 56 58 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/2848f231-9422-462d-a59e-966602783b8a)



A CNN model is defined using TensorFlow and Keras. The model consists of several convolutional layers with max-pooling, activation functions, and dropout layers to prevent overfitting. The model architecture is outlined in the code.

## Model Training

The model is compiled and trained using the training dataset. Training history (including loss and accuracy) is stored for visualization.

## Transfer Learning

Two pre-trained models, ResNet50V2 and InceptionV3, are fine-tuned for image classification. The top layers of these models are removed, and a new classification head is added.

## Model Comparison

The performance of the base CNN model and the two transfer learning models (ResNet50V2 and InceptionV3) is compared regarding loss and accuracy.

![Screenshot 2023-09-16 at 2 16 23 AM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/f2d9fbe6-ad9d-427d-ad1c-059362813569)


## Conclusion

In conclusion, we observe the critical role of transfer learning in image classification. It highlights that fetching pre-trained weights not only expedites model training but also significantly enhances accuracy. This approach demonstrates the power of leveraging existing knowledge to tackle complex tasks effectively.

## Tools Used

![Screenshot 2023-09-14 at 10 58 19 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/4e7364c5-df31-400e-ac4b-761d1cd264db)      ![Screenshot 2023-09-14 at 10 59 23 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/c9ddf2f9-81dd-4e3e-a1c9-d366300c8cbb)      ![Screenshot 2023-09-14 at 10 58 58 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/806665c6-0d69-4fcd-a830-17ca9fde67dd)



