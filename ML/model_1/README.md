# Obesity Level Prediction Model

This repository contains a machine learning model that predicts obesity levels based on personal attributes, lifestyle, and dietary habits. The model is built using TensorFlow/Keras and is designed to be deployed as an API for real-time predictions.

---

## **Features**

The dataset includes the following features:
- **Gender**: Categorical (Male, Female)
- **Age**: Continuous
- **Height**: Continuous
- **Weight**: Continuous
- **Family History with Overweight**: Binary
- **High-Calorie Food Consumption**: Binary
- **Vegetable Consumption Frequency**: Integer
- **Number of Meals per Day**: Continuous
- **Food Between Meals**: Categorical
- **Smoking Habit**: Binary
- **Water Consumption (Liters/Day)**: Continuous
- **Calorie Monitoring**: Binary
- **Physical Activity Frequency**: Continuous
- **Technology Usage Time (Hours/Day)**: Integer
- **Alcohol Consumption Frequency**: Categorical
- **Transportation Mode**: Categorical

The target variable is the **Obesity Level**, categorized into various levels such as:
- Normal Weight
- Overweight Level I
- Overweight Level II
- Obesity Types I, II, III

---

## **Model Architecture**

- Input Layer: 16 features (preprocessed and scaled)
- Hidden Layers:
  - Dense (64 units, ReLU activation, Batch Normalization, Dropout)
  - Dense (128 units, ReLU activation, Batch Normalization, Dropout)
  - Dense (64 units, ReLU activation, Batch Normalization, Dropout)
- Output Layer:
  - Dense (Number of obesity classes, Softmax activation)
- Loss Function: Categorical Crossentropy
- Optimizer: Adam
- Metrics: Accuracy

---

## **Results**

- **Test Accuracy**: 91.48%
- **Test Loss**: 0.23

The model performs well with a high classification accuracy on the test dataset.

---

## **How to Run**

### 1. **Clone the Repository**
```bash
git clone https://github.com/Faisal12104/eatRight
cd eatRight/model_1
```

### 2. **Install Dependencies**
Ensure Python 3.9+ is installed, and then install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. **Run the Flask API**
Start the API server:
```bash
OC_deploys.py
```

### 4. **Test the API**
Use `curl` or a tool like Postman to send POST requests to the API:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "features": [
    -0.5082512769523888,
    0.21708608747503674,
    0.4166879186309691,
    0.7025637659198204,
    1.3715296537859547,
    0.6971408355703766,
    -3.1628226450823056,
    -1.2012308355442176,
    -0.3732090562703104,
    0.6762367368859359,
    -1.0412561997824246,
    0.0967646493526264,
    1.3639655231547303,
    0.8009764911986628,
    0.6764400612809583,
    2.489748360679963
  ]
}' http://localhost:5500/predict
```

The response will include the predicted obesity level.
