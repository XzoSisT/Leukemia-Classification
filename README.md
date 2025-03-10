# Leukemia Classification Project

This project is a deep learning-based application for leukemia classification using microscopic images. The system detects and classifies cells as "HEM" (normal) or "ALL" (leukemia) with high accuracy, based on EfficientNetV2.

---
## Dataset
### About this dataset
Acute lymphoblastic leukemia (ALL) is the most common type of childhood cancer and accounts for approximately 25% of the pediatric cancers.
These cells have been segmented from microscopic images and are representative of images in the real-world because they contain some staining noise and illumination errors, although these errors have largely been fixed in the course of acquisition.

The task of identifying immature leukemic blasts from normal cells under the microscope is challenging due to morphological similarity and thus the ground truth labels were annotated by an expert oncologist.

In total there are 15,135 images from 118 patients with two labelled classes:
- Normal cell
- Leukemia blast

[Dataset Link](https://www.kaggle.com/datasets/andrewmvd/leukemia-classification)
---

## 🌟 Features
- **Image Prediction**: Upload cell images to classify them as leukemia or normal.
- **Progress Bar**: Displays the confidence level of the prediction.
- **Interactive UI**: A simple, user-friendly web interface built with Flask.
- **Advanced Deep Learning**: Utilizes TensorFlow and pre-trained EfficientNetV2 for image classification.
---
## Technology used
- **Programming Languages**: Python
- **Deep Learning Framework**: TensorFlow 2.11
- **Web Framework**: Flask
- **Data Visualization**: Matplotlib, Seaborn
- **Image Processing**: OpenCV, PIL
- **Machine Learning Utilities**: scikit-learn
---
## Model Architecture
```bash
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 efficientnetv2-b3 (Function  (None, 1536)             12930622  
 al)                                                             
                                                                 
 batch_normalization (BatchN  (None, 1536)             6144      
 ormalization)                                                   
                                                                 
 dense (Dense)               (None, 256)               393472    
                                                                 
 dropout (Dropout)           (None, 256)               0         
                                                                 
 dense_1 (Dense)             (None, 2)                 514       
                                                                 
=================================================================
Total params: 13,330,752
Trainable params: 13,218,464
Non-trainable params: 112,288
_________________________________________________________________
```
---
# How to Run Leukemia Classification Project

Follow these steps to set up and run the project locally:

## 1️⃣ Clone the Repository
Clone this repository from GitHub to your local machine using the following commands:
```bash
git clone https://github.com/YourUsername/Leukemia-Classification.git
cd Leukemia-Classification

```
## 2️⃣ Install Dependencies
Install the required Python packages for the project:
```bash
pip install -r requirements.txt
```
## 3️⃣ Run the Web Application
Start the Flask server by running:
```bash
python run.py
```
## 4️⃣ Open the Web Interface
Once the server is running, navigate to the following URL in your web browser:
```bash
http://127.0.0.1:5000/
```
---
## Preview Web App
![image](https://github.com/user-attachments/assets/5d276ad2-11d3-443e-aa5a-db88ca1f342d)
![image](https://github.com/user-attachments/assets/14c8f334-1141-44f9-96a2-3514f4988503)
![image](https://github.com/user-attachments/assets/beb3e64d-1d38-428c-9d8d-12ad141c4fe4)


