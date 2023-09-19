# Chest X-Ray Pneumonia Prediction

![Screenshot 2023-09-19 at 11 30 34 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/9be16ef9-e09c-4783-9730-17e86a09e69c)

## Overview
This repository contains a machine learning project for the prediction of pneumonia in chest X-ray images. Pneumonia is a common and potentially life-threatening respiratory infection, and early and accurate diagnosis is crucial for effective treatment. This project leverages deep learning techniques to assist healthcare professionals in diagnosing pneumonia from chest X-ray images.

## Introduction

Pneumonia is a prevalent respiratory infection that can affect people of all ages. This project aims to automate the detection of pneumonia in chest X-ray images using a deep learning model.

## Dataset Preparation

We collected our dataset from https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia.

We used the TensorFlow Datasets API to load and preprocess the images. The dataset is divided into "NORMAL" and "PNEUMONIA" classes, with corresponding labels.

## Model

For this project, we utilized the ResNet50V2 deep convolutional neural network (CNN) architecture as our backbone model. The top layer of the ResNet50V2 model has been set to `False`, allowing us to fine-tune the model for pneumonia detection. Here's a summary of our model:

![Screenshot 2023-09-19 at 11 41 25 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/e14fc0d3-4e89-4629-b429-d782980c3552)

Optimizer: Adam (learning rate = 0.001, beta_1 = 0.9, beta_2 = 0.999)
Loss Function: Binary Crossentropy
Metrics: Accuracy, Precision, Recall

We applied the following callbacks during training:
ModelCheckpoint: To save the best weights during training.
EarlyStopping: To stop training early if no improvement is observed.
To train the model, we used the prepared datasets with a batch size of 32 and trained for 8 epochs.


## Training

![Screenshot 2023-09-20 at 4 22 13 AM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/afcdd827-752b-49e6-9348-079b3ccf5c3c)

![Screenshot 2023-09-20 at 4 31 04 AM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/9fed647f-5727-4d3f-8886-c97d13526eca)



## Results

![Screenshot 2023-09-20 at 4 46 51 AM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/5ef8664c-5585-4b78-965a-e20420d115d4)

In medical predictions, especially in diagnostic tests and disease detection, recall is a critical and often the most important metric. Our model has an excellent recall, hence it has performed well in that regard. Some improvements could be made to other metrics by increasing the number of epochs or adding more layers with dropout running on GPU.

## Tools Used
![Screenshot 2023-09-19 at 11 46 08 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/e822fc84-48d9-4329-901f-81d7a9035692)![Screenshot 2023-09-19 at 11 46 21 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/91ed77a3-e2d5-490d-a26e-0c54ee55a6ce)![Screenshot 2023-09-19 at 11 45 57 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/419239d6-ed0f-4594-be79-c0de6fc90618)














