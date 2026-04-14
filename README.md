# 🎓 Placement Insight — AI-Powered Student Placement Predictor

> A machine learning web application that predicts whether a student will be placed based on **8 academic and behavioral indicators**. Trained on **10,000 student records**, built with **Flask** and **scikit-learn**, and deployed live on **Render**.

---

## 🔗 Live Demo

🌐 **Deployed on Render:** [https://placement-insight.onrender.com]

---

## 📌 Project Overview

**Placement Insight** is a full-stack machine learning application that takes a student's academic profile as input and predicts their placement likelihood (`Placed` / `Not Placed`). Two models were trained and evaluated — **Logistic Regression** (89.07% accuracy) and **Decision Tree** (100% accuracy — flagged as overfitting). The Logistic Regression model was chosen for production deployment, serialized as `model.pkl`, and served via a Flask API.

---

## 🧠 How It Works

```
User Input (8 features via web form)
        ↓
Flask Backend (/predict route)
        ↓
numpy array of shape (1, 8) formed from form data
        ↓
Loaded scikit-learn Logistic Regression model (model.pkl) makes prediction
        ↓
Result rendered back to index.html via Jinja2 template
```

---

## 🗂️ Project Structure

```
Render-ML/
│
├── app.py                        # Flask application — routes: / and /predict
├── model.pkl                     # Trained & serialized Logistic Regression model
├── Placement_prediction.ipynb    # Full ML notebook: EDA → training → evaluation
├── requirements.txt              # Python dependencies
│
├── templates/
│   └── index.html                # Responsive frontend UI with Jinja2 templating
│
└── .gitignore
```

---

## 🔢 Dataset

| Property | Value |
|---|---|
| **Source file** | `CollegePlacement.csv` |
| **Total rows** | 10,000 |
| **Total columns** | 10 |
| **Null values** | None |
| **Train set** | 7,000 rows (70%) |
| **Test set** | 3,000 rows (30%) |
| **random_state** | 42 |

---

## 🔢 Input Features

The model takes **8 student metrics** as input (after dropping `College_ID`):

| Feature | Description | Type | Range |
|---|---|---|---|
| `IQ` | Intelligence Quotient score | Integer | 41–158 |
| `Prev_Sem_Result` | Previous semester GPA/score | Float | 5.0–10.0 |
| `CGPA` | Cumulative Grade Point Average | Float | 4.54–10.46 |
| `Academic_Performance` | Overall academic performance rating | Integer (1–10) | 1–10 |
| `Internship_Experience` | Has internship? (0 = No, 1 = Yes) | Binary | 0 or 1 |
| `Extra_Curricular_Score` | Score representing extracurricular participation | Integer (0–10) | 0–10 |
| `Communication_Skills` | Communication skills score | Integer (1–10) | 1–10 |
| `Projects_Completed` | Number of academic/personal projects | Integer (0–5) | 0–5 |

---

## ⚙️ ML Pipeline

### 1. Preprocessing
- Copied dataset (`data_cp = data.copy()`)
- Applied **`LabelEncoder`** to:
  - `Internship_Experience` (No → 0, Yes → 1)
  - `Placement` (No → 0, Yes → 1)
- Dropped `College_ID` (non-predictive identifier)
- Verified zero null values across all columns

### 2. EDA
- Inspected dataset shape: `(10000, 10)`
- Visualized outliers using **seaborn boxplot** — IQ column contains outliers

### 3. Models Trained

| Model | Test Accuracy | Notes |
|---|---|---|
| **Logistic Regression** | **89.07%** | Selected for deployment; ConvergenceWarning observed |
| Decision Tree | 100.00% | Overfitting — perfect confusion matrix, not deployed |

### 4. Logistic Regression — Detailed Evaluation

**Confusion Matrix:**
```
Actual \ Predicted |  0   |  1
-------------------|------|-----
         0         | 2396 | 115
         1         |  213 | 276
```

**Classification Report:**
```
              precision    recall  f1-score   support
           0       0.92      0.95      0.94      2511
           1       0.71      0.56      0.63       489
    accuracy                           0.89      3000
   macro avg       0.81      0.76      0.78      3000
weighted avg       0.88      0.89      0.89      3000
```

> **Note on class imbalance:** ~83.7% of students were Not Placed vs 16.3% Placed. This causes lower recall (0.56) for the "Placed" class.

---

## 🤖 ML Model

- **Algorithm:** `LogisticRegression()` from scikit-learn
- **Serialization:** Saved using Python `pickle` as `model.pkl`
- **Prediction Output:** Binary — `Placed` (1) or `Not Placed` (0)
- **Input:** `numpy` array of shape `(1, 8)` from form submission
- **Known Issue:** ConvergenceWarning — lbfgs solver did not fully converge. Fix: increase `max_iter` or scale features with `StandardScaler`.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **ML** | scikit-learn (LogisticRegression, DecisionTreeClassifier, LabelEncoder), numpy, pandas |
| **EDA / Visualization** | matplotlib, seaborn |
| **Frontend** | HTML5, CSS3, Jinja2 templating |
| **Server** | Gunicorn (production WSGI server) |
| **Deployment** | Render (cloud platform) |

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/bonunithinkumar/Render-ML.git
cd Render-ML
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv myenv
source myenv/bin/activate       # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

**3. Run the Flask app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## ☁️ Deployment — Render

This app is deployed on [Render](https://render.com) using the following configuration:

| Setting | Value |
|---|---|
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Environment** | Web Service |

> `gunicorn` is used as the production WSGI server instead of Flask's built-in development server.

---

## 📡 API Endpoints

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Renders the home page with the prediction form |
| `POST` | `/predict` | Accepts 8 form fields, runs Logistic Regression model, returns prediction |

---

## 📊 Key Design Decisions

- **Two models trained, one deployed** — Trained both Logistic Regression and Decision Tree. Decision Tree hit 100% accuracy (overfitting), so Logistic Regression (89.07%) was chosen for production.
- **`os.path` for model loading** — `os.path.dirname(os.path.abspath(__file__))` ensures `model.pkl` resolves correctly regardless of where the app is run from — critical for cloud deployment.
- **LabelEncoder for categorical columns** — `Internship_Experience` (Yes/No) and `Placement` (Yes/No) were encoded to 0/1 before training.
- **Jinja2 conditional rendering** — Prediction result is conditionally rendered using `{% if prediction_text %}`, ensuring a clean UI on first load.
- **Gunicorn in requirements** — Production-grade WSGI server explicitly included for Render compatibility.

---

## 🔮 Future Improvements

- [ ] Fix Logistic Regression ConvergenceWarning — increase `max_iter` or add `StandardScaler`
- [ ] Address class imbalance using SMOTE or `class_weight='balanced'`
- [ ] Add probability score (`.predict_proba()`) to the prediction output
- [ ] Include model explainability (SHAP values) for each prediction
- [ ] Switch from pickle to joblib for safer model serialization
- [ ] Add input validation with user-friendly error messages
- [ ] Add a REST API endpoint returning JSON (for mobile/API consumers)
- [ ] Add model retraining pipeline as new placement data becomes available

---

## 👤 Author

**Nithin Kumar Bonu**
- GitHub: [@bonunithinkumar](https://github.com/bonunithinkumar)
- Deployed via: [Render](https://render.com)

---

*© 2025 Placement Insight • Data Intelligence Unit*
