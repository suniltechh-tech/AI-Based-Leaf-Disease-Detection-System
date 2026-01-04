🌿 Leaf Disease Detection System

An AI-powered Leaf Disease Detection System that identifies plant diseases from leaf images using Deep Learning techniques.
This project helps farmers and researchers detect plant diseases early and improve crop productivity.

📌 Project Overview

Plant diseases are one of the major causes of crop loss worldwide. Manual inspection of leaves is time-consuming and requires expert knowledge.
This system automates the process by analyzing leaf images and predicting the disease class using a Convolutional Neural Network (CNN).

🎯 Objectives

Detect plant leaf diseases automatically

Reduce dependency on manual inspection

Provide fast and accurate disease prediction

Support smart agriculture initiatives

🧠 Technology Stack

Programming Language: Python

Deep Learning Framework: TensorFlow / Keras

Image Processing: OpenCV

Model Type: Convolutional Neural Network (CNN)

Deployment (Optional): Streamlit / Flask

📂 Project Structure
Leaf-Disease-Detection-System/
│
├── app.py                 # Application file
├── model.h5               # Trained CNN model
├── dataset/               # Leaf images dataset
│   ├── healthy/
│   ├── diseased/
│
├── requirements.txt       # Required libraries
├── README.md              # Project documentation

🗃 Dataset Information

Dataset contains images of healthy and diseased leaves

Images are resized and normalized before training

Data augmentation is applied to improve accuracy

You can use public datasets like:

PlantVillage Dataset

⚙️ How It Works

User uploads a leaf image

Image is preprocessed (resize, normalization)

CNN model extracts features from the image

Model predicts the disease class

Result is displayed to the user

🚀 Installation & Execution
Step 1: Clone the Repository
git clone https://github.com/your-username/Leaf-Disease-Detection-System.git

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Application
python app.py

📊 Model Performance

Uses CNN for feature extraction

Achieves high accuracy on test data

Robust against variations in leaf color and size

🌱 Future Enhancements

Add more plant species and diseases

Improve accuracy using transfer learning

Deploy as a mobile or web application

Provide disease treatment suggestions

👨‍💻 Author
