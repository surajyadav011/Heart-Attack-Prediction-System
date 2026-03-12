# Heart Attack Prediction System

An end-to-end machine learning web application that predicts the probability of heart attack risk using patient clinical parameters.

The project combines Machine Learning, Flask API development, and an interactive web dashboard to create a real-time cardiovascular risk prediction tool.

---

# Project Overview

CardioSense analyzes patient medical data and predicts the likelihood of heart attack using a trained machine learning model.

Users input 13 clinical parameters and the system returns:

• Heart attack risk prediction  
• Probability score  
• Visual risk analysis

---

# Business Problem

Cardiovascular diseases remain one of the leading causes of death globally.

Doctors must analyze multiple clinical variables to determine patient risk, which can be complex and time-consuming.

This project demonstrates how machine learning can assist healthcare professionals in predicting cardiovascular risk more efficiently.

---

# Dataset Description

Source: Public medical dataset (UCI / Kaggle Heart Disease Dataset)

Dataset contains patient clinical information used for heart disease diagnosis.

Features:

| Feature | Description |
|-------|-------------|
| age | Age of patient |
| sex | Gender |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Cholesterol level |
| fbs | Fasting blood sugar |
| restecg | ECG result |
| thalach | Maximum heart rate |
| exang | Exercise induced angina |
| oldpeak | ST depression |
| slope | Slope of ST segment |
| ca | Major vessels |
| thal | Thalassemia type |

Target variable:

Heart attack risk (0 = No Risk, 1 = High Risk)

---

# ❤️ Heart Attack Prediction System

## Main Interface
![Main Interface](preview-of-heart-prediction.png)

## Prediction Output Example
![Prediction Output](preview-of-heart-attack-prediction-output.png)

## Code Preview

### Code Preview 1
![Code Preview 1](code-preview-1.png)

### Code Preview 2
![Code Preview 2](code-preview-2.png)

### Code Preview 3
![Code Preview 3](code-preview-3.png)



# Tools and Technologies

Python  
Machine Learning  
Flask API  
NumPy  
Scikit-Learn  
HTML  
CSS  
JavaScript  
Chart.js

---

### Project Structure and how to use 

All files inside main  heart_prediction  folder and HTML inside templates.

structure
```
heart-attack-prediction/
│
├── app.py
├── app2.py
│
├── Heart_attack_prediction.pkl
│
├── notebooks/
│   ├── real_ml_project.ipynb
│   └── APP.ipynb
│
├── templates/
│   └── index.html
```

## How to Run the Project

Make sure all required Python libraries are installed and run all the code in the Jupyter Notebook files before executing the project.

1. Go to the **heart_prediction** project folder.

2. In the folder path bar, type:

cmd

Press **Enter** to open Command Prompt in that folder.

3. Make sure all required Python libraries are installed.

4. In CMD, run the application:

python app2.py

5.then type  python app2.py

6. After running the command, you will see a link like this:

http://127.0.0.1:5000/

7. Hold **Ctrl** and click the link, or copy it into your browser.

The **Heart Attack Prediction System** will open in your browser.


# Data Cleaning and Preparation

Steps performed:

• Removed missing values  
• Feature scaling using Min-Max normalization  
• Data splitting for training and testing  
• Model training using machine learning algorithms  
• Model evaluation using classification metrics

---

# Dashboard Features

• Interactive clinical parameter input form  
• Real-time prediction system  
• Probability breakdown visualization  
• Risk classification output  
• Chart.js risk visualization

---

# Key Insights

The model identifies the relationship between cardiovascular risk and factors such as:

• Chest pain type  
• Exercise induced angina  
• Maximum heart rate  
• ST depression values  
• Major vessels count

These features significantly influence heart disease prediction.

---

# Business Impact

The system demonstrates how machine learning can assist healthcare professionals in:

• Early risk detection  
• Faster diagnosis  
• Preventive healthcare decision making

---

# Skills Demonstrated

Machine Learning Modeling  
Data Preprocessing  
Model Deployment  
Flask API Development  
Frontend Integration  
Data Visualization

---

# Future Improvements

• Add more medical datasets  
• Implement deep learning models  
• Deploy using Docker / Cloud  
• Add patient history tracking  
• Improve model accuracy

---

# Author

Suraj  
Data Science & Machine Learning Enthusiast
