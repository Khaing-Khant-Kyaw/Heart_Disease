## Heart Disease Prediction and Risk Analysis Using Machine Learning with Web-Based Application

This repository contains the implementation of a project focused on predicting heart disease using various machine learning algorithms. The project was developed as part of the 6500CSMM module under the supervision of Dr. Yuzana Win, submitted to Liverpool Johnmoores University.

## Project Overview

Heart disease is a major global health concern, and early detection is crucial for improving patient outcomes. This project aims to build accurate machine learning models to predict heart disease using a comprehensive dataset that includes several potential predictors. The best-performing model is deployed in a user-friendly web application to make the prediction tool accessible to users.

The flowchart illustrates the steps taken in the system, starting from user data input in the web application, followed by preprocessing and feature extraction, and then passing through the trained machine learning model to generate a prediction. Finally, the result is displayed to the user.

# Flow Chart

![Flow Chart](https://github.com/Khaing-Khant-Kyaw/Heart_Disease/blob/main/Flow%20Chart.jpg)

## Features

- **Data preprocessing and cleansing**: Data preparation steps including merging multiple datasets and handling missing values.
- **Machine learning models**: Several machine learning algorithms are implemented and evaluated, including:
  - Logistic Regression
  - Random Forest Classifier
  - Decision Tree
  - K-Nearest Neighbors
  - Neural Networks
- **Model selection and evaluation**: The models are trained using different train-test split ratios (90/10, 80/20, 70/30) and evaluated based on accuracy scores.
- **Web application**: The best-performing model (Random Forest Classifier) is deployed using Flask, creating a simple web app that allows users to input health data and receive heart disease predictions.
  
## Technologies Used

- **Programming Languages**: Python
- **Libraries**: Scikit-learn, Flask, Pandas, NumPy, Matplotlib
- **Web Framework**: Flask
- **Data Visualization**: Matplotlib
- **Machine Learning Algorithms**: Scikit-learn
- **Deployment**: Localhost using Flask
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   
2. Navigate to the project directory:
   cd heart-disease-prediction

3. Install the required dependencies:
   pip install -r requirements.txt

## Usage
1. Run the Flask web application:
   python app.py

2. Open your browser and navigate to http://localhost:5000.
   Input your health data to receive a prediction of whether you are at risk of heart disease.

3. Input your health data to receive a prediction of whether you are at risk of heart disease.

## Results
**Best Model: Random Forest Classifier**

  -Train-Test Split: 90/10
  
  -Accuracy: 92% (on the best split)
  
**Future Work**

  -Improve model accuracy by incorporating more advanced machine learning techniques.
  
  -Develop real-time monitoring systems to continuously update predictions.
  
  -Enhance the web application for broader accessibility and usability.
  
## Conclusion
This project demonstrates the potential of machine learning algorithms to predict heart disease, contributing to the healthcare domain by providing a tool that aids in early detection. By testing multiple models and implementing the Random Forest Classifier, we achieved high accuracy and made the prediction process accessible via a web application. With further development, the model can be refined to support real-time data and offer even more accurate predictions, helping healthcare professionals and individuals alike.


## Project Thesis

If you're interested in learning more about the project, you can read the full thesis document [here](https://github.com/Khaing-Khant-Kyaw/Heart_Disease/blob/main/Heart%20Disease%20Prediction%20Thesis%20.pdf).









