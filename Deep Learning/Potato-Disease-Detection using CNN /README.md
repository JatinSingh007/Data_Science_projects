# Machine Learning-Based Crop Disease Detection for Indian Agriculture

![Screenshot 2023-09-06 at 10 51 47 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/7b25b157-7ccd-4c1d-83ad-a2bb5a4d64bf)

## Introduction

The global challenge of feeding a rapidly growing population, expected to reach over 9 billion people by 2050, necessitates a significant increase in food production. Agriculture plays a pivotal role in this endeavor, with India being a major contributor to the world's agricultural output. However, infectious diseases pose a significant threat to crop yields, resulting in substantial losses. In India, where agriculture is a cornerstone of the economy, these losses are particularly concerning.

## Statistics on Agriculture in India

Agriculture contributes approximately 17-18% of India's GDP.
Over 50% of India's population depends on agriculture for their livelihood.
India is one of the world's largest producers of key crops such as rice, wheat, and potatoes.

## Current Challenges

Infectious diseases have a devastating impact on crop yields in India, with an average reduction of 40% across various crops. Some farmers in the developing world experience even higher losses, up to 100%. This situation is especially dire for potato crops, which are vital for food security and economic stability in India.

## Proposed Solution

To address this pressing issue, we propose the development of a beta Machine Learning Model that focuses on detecting the stage of infection in potato leaves. This model leverages computer vision technology to provide a rapid and accurate assessment of crop health. By creating a user-friendly web or mobile application, we aim to empower farmers to take photos of their crops and receive instant feedback regarding the presence and severity of disease. The model will classify the potato leaves into three classes: "PotatoEarly" (early-stage infection), "PotatoHealthy" (disease-free), and "PotatoLate" (advanced-stage infection).

## Expected Impact

### Empowering Farmers

The application will provide farmers with a simple tool to monitor and manage their crops more effectively.

### Reducing Yield Losses

Timely identification of diseased crops will enable farmers to take appropriate actions, potentially reducing yield losses significantly.

### Economic Growth

Increased crop productivity will contribute to the overall growth of the Indian economy by enhancing agricultural output and food security.

### Data Collection

The application will also serve as a valuable source of data on disease prevalence, aiding researchers and policymakers in devising targeted interventions to combat crop diseases.

## Architecture

![Screenshot 2023-09-04 at 9 34 01 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/d18f1aca-8fbb-4e13-a1ce-086111a42edc)

### Data Fetching & Preprocessing
 
 #### Data Fetching with tf.Dataset
    
  I've used TensorFlow's tf.data.Dataset to fetch my data. This is a good practice, especially when dealing with large datasets, as it allows me to work with data in batches rather than loading the entire dataset into memory at once.

#### Image Size Standardization
     
  I've specified a specific image size when fetching the data. This is essential for consistency during training because deep learning models require all input images to have the same dimensions. It also helps prevent potential errors that can occur when working with images of different sizes.

#### Data Augmentation
     
   Data augmentation is a crucial technique to increase the robustness and generalization of my model. I've applied data augmentation techniques like RandomFlip, RandomRotation, Resizing, and Rescaling. These augmentations help generate variations of my dataset, making the model more resilient to different input conditions.

#### Data Splitting
     
  I've split my dataset into training, validation, and testing sets, following the standard practice. An 80% training set and a 10% validation set are common splits. The remaining 10% is used for testing.

#### Caching and Prefetching

  I've used tf.cache to cache the dataset in memory or local storage, which helps avoid repeated file opening and reading operations. Additionally, I've employed tf.prefetch to overlap data preprocessing and model execution. This optimization minimizes the step time and ensures efficient data loading during training.
     
  ![Screenshot 2023-09-06 at 10 36 28 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/136b776b-9684-4650-882d-5810305fc5c7)
     
  ![Screenshot 2023-09-06 at 10 39 54 PM](https://github.com/JatinSingh007/Data_Science_projects/assets/54170834/288df440-b1f8-46ae-88fa-83c27b37e366)


