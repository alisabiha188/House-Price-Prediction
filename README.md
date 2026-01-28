# House Price Prediction App

A simple **machine learning web app** that predicts house prices based on basic house details. The app is built using **Streamlit** and a trained ML regression model.

---

##  Project Files

```
app.py                         # Streamlit app
house_price_prediction.ipynb   # Model training notebook
housepre_model.pkl             # Saved trained model
Housing.csv                    # Dataset
README.md                      # Project description
```

---

##  Dataset

* File: `Housing.csv`
* Contains house details and their prices
* Used to train the machine learning model

### Features Used

* Area (sq ft)
* Bedrooms
* Bathrooms
* Stories
* Main Road (Yes/No)
* Guest Room (Yes/No)
* Basement (Yes/No)
* Hot Water Heating (Yes/No)
* Air Conditioning (Yes/No)
* Parking
* Preferred Area (Yes/No)
* Furnishing Status

---

## Machine Learning Model

* Trained using **scikit-learn**
* Categorical values are encoded into numbers
* Model is saved as `housepre_model.pkl`
* The model predicts house price based on user input

---

## Streamlit App

The Streamlit app allows users to:

* Enter house details
* Click **Predict Price**
* Get an estimated house price instantly

---
## How to Run the App

### 1. Install required libraries

```bash
pip install streamlit numpy pandas scikit-learn joblib
```

### 2. Run the app

```bash
streamlit run app.py
```

### 3. Open in browser

```
http://localhost:8501
```

---

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy



