# 🧬 Health Insurance Cost Prediction

This project predicts individual medical insurance costs based on personal health and demographic data using a trained machine learning model.

---

## 💡 Problem Statement

Medical costs can vary significantly depending on a person's age, BMI, smoking status, region, and other factors. Accurately estimating these costs helps insurers, hospitals, and individuals plan better.

---

## 📄 Dataset

- Total records: 1,339 people
- Attributes:
  - **age**: Age of the person
  - **sex**: Male or Female
  - **bmi**: Body mass index
  - **children**: Number of children
  - **smoker**: Yes or No
  - **region**: Northeast, Northwest, Southeast, Southwest
  - **charges**: Medical insurance cost

---

## ⚙️ Approach

- Converted categorical variables (sex, smoker, region) into numerical values.
- Split data into training and testing sets.
- Trained a **Gradient Boosting Regressor (GBR)** for better accuracy.
- Evaluated using MAE, MSE, and R² Score.

---

## 💻 Technologies Used

- Python
- scikit-learn
- Flask (for API)
- Tkinter (for GUI)
- Pandas
- Joblib

---

## 🚀 Features

- 📈 **Backend API**: Flask API endpoint `/predict` to get insurance cost predictions via JSON request.
- 💻 **Desktop GUI**: User-friendly Tkinter application for local predictions.
- ✅ Input validation to ensure correct data.

---

## 🧪 Performance

- **MAE**: ~2447
- **MSE**: ~18,944,595
- **R² Score**: ~0.88

---

## 🛡️ Security Note

This project does **not** include authentication since it's for local demonstration only. In production, API keys or token-based authentication should be added.

---

## 🗺️ Folder Structure

```
insurance_cost_prediction/
├── insurance.csv
├── preprocessing_and_training.py
├── app.py
├── gui_app.py
├── requirements.txt
├── README.md
└── venv/
```


---

## 💥 How to Run

### 1️⃣ Setup

```bash
python -m venv venv
# Activate
venv\Scripts\activate     # Windows
# Install dependencies
pip install -r requirements.txt

2️⃣ Train model

python preprocessing_and_training.py

3️⃣ Run GUI

python gui_app.py

4️⃣ Run API

python app.py

Test using Postman or PowerShell:

{
    "age": 45,
    "sex": "male",
    "bmi": 30.5,
    "children": 2,
    "smoker": "no",
    "region": "northeast"
}
```

🏆 Future Improvements

Add API authentication

Containerize using Docker

Deploy to cloud (AWS, Azure, etc.)

Improve feature engineering and hyperparameter tuning


🙏 Acknowledgments

Thanks to the open dataset available for learning and exploration.


