# RideWise Customer Analytics and Churn Prediction System

## Overview

RideWise is a leading European mobility technology company serving over **200,000 customers** and powering more than **800,000 monthly trips** across major cities. The company operates in the fast-paced European mobility and transportation technology sector, providing innovative solutions to address evolving urban transit needs.

The fictional RideWise operates across five major European cities:

* London
* Berlin
* Amsterdam
* Barcelona
* Milan

With a rapidly growing customer base and strong operational footprint, RideWise is positioned as a market leader in mobility technology. However, the company faces increasing challenges with customer retention, promotion effectiveness, and customer behavior analysis.

This project develops an end-to-end machine learning solution to predict customer churn, segment customers, and provide real-time customer risk assessment using modern data science and deployment techniques.

---

## Business Challenge

RideWise currently faces several business challenges:

* High quarterly customer churn rate of approximately **25%**
* Limited understanding of customer behavioral patterns
* Low promotion uptake rates and unclear campaign ROI
* No predictive capability to identify at-risk customers before churn
* Manual customer analysis processes that take weeks
* Lack of real-time customer insights for operational decision making
* No integrated analytics system for portfolio-level performance tracking
* Increasing competitive pressure requiring data-driven customer retention strategies

---

## Project Objectives

The objectives of this project are to:

1. Develop customer churn prediction models using machine learning algorithms.
2. Build a customer segmentation system using clustering techniques.
3. Implement a feature engineering pipeline for customer behavioral data.
4. Create a model interpretability framework using business-friendly explanations.
5. Deploy real-time scoring capabilities for customer risk assessment.
6. Build a customer analytics dashboard and reporting framework.
7. Demonstrate API development methodology for model deployment.
8. Create a production-ready system with basic monitoring capabilities.

---

## Dataset Description

The dataset contains customer demographic information, trip history, engagement metrics, promotional activities, and behavioral indicators collected from RideWise customers across five European cities.

Key categories include:

* Customer demographics
* Ride frequency and trip statistics
* Promotion and discount usage
* Customer engagement metrics
* Transaction history
* Geographic information
* Behavioral features
* Customer churn status

---

## Machine Learning Workflow

The project follows a complete machine learning lifecycle:

### 1. Data Preparation

* Data cleaning and preprocessing
* Missing value handling
* Outlier treatment
* Categorical encoding
* Feature scaling

### 2. Feature Engineering

* Customer behavioral metrics
* Trip frequency indicators
* Customer engagement scores
* Promotion responsiveness measures
* Historical activity features

### 3. Model Development

Machine learning models developed include:

* Logistic Regression
* Random Forest Classifier

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

## Customer Segmentation

Customer segmentation techniques are implemented to identify distinct customer groups based on:

* Riding frequency
* Spending behavior
* Promotion responsiveness
* Engagement levels
* Geographic location

These segments support targeted marketing and personalized retention strategies.

---

## Model Interpretability

The project incorporates model explainability techniques to provide business-friendly insights, including:

* Feature Importance Analysis
* SHAP (SHapley Additive Explanations)
* Business interpretation of key churn drivers

This allows stakeholders to understand why customers are predicted to churn and supports data-driven decision making.

---

## Deployment

The project demonstrates deployment through:

### Streamlit Application

A web-based dashboard for:

* Customer risk scoring
* Churn prediction
* Customer analytics visualization
* Interactive business insights

### FastAPI REST API

The API provides:

* Real-time prediction endpoints
* JSON-based request and response handling
* Integration capability with external systems
* Production-ready architecture

---

## Project Structure

```text
RideWise-Customer-Analytics/

├── Data/
│   └── Raw and processed datasets
│
├── Model/
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   └── Exploratory analysis and model development
│
├── app.py
│   └── Streamlit application
│
├── inference.py
│   └── FastAPI inference API
│
├── requirements.txt
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd RideWise-Customer-Analytics
```

Create a virtual environment:

```bash
python -m venv nova-venv
```

Activate the environment:

**Windows**

```bash
.\nova-venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Streamlit Dashboard

```bash
streamlit run app.py
```

### FastAPI API

```bash
python -m uvicorn inference:app --reload
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* Advanced ensemble learning models
* Automated retraining pipeline
* Cloud deployment using Docker and Kubernetes
* Real-time streaming predictions
* A/B testing framework for promotion optimization
* Continuous model monitoring and drift detection

---

## Author

**Sunday Temitope**

MSc Data Science | Machine Learning & Analytics Enthusiast

GitHub: https://github.com/SUNDAYTITILAYO

---

## Disclaimer

RideWise is a fictional company created for educational and portfolio purposes. The project demonstrates practical applications of machine learning, customer analytics, and model deployment in the mobility technology domain.
