# 🎓 Placement Insight — AI-Powered Student Placement Predictor

> A machine learning web application that predicts whether a student will be placed based on 8 academic and extracurricular indicators. Built with **Flask**, **scikit-learn**, and deployed live on **Render**.

---

## 🔗 Live Demo

🌐 **Deployed on Render:** [https://placement-insight.onrender.com]

---

## 📌 Project Overview

**Placement Insight** is a full-stack machine learning application that takes a student's academic profile as input and predicts their placement likelihood (`Placed` / `Not Placed`). The model was trained on a real-world-style dataset containing student metrics, then serialized and served via a Flask API with a responsive frontend UI.

---

## 🧠 How It Works

```
User Input (8 features)
        ↓
Flask Backend (/predict route)
        ↓
numpy array formed from form data
        ↓
Loaded scikit-learn model (model.pkl) makes prediction
        ↓
Result rendered back to index.html via Jinja2 template
```

---

## 🗂️ Project Structure

```
Render-ML/
│
├── app.py                  # Flask application — routes: / and /predict
├── model.pkl               # Trained and serialized ML model (scikit-learn)
├── requirements.txt        # Python dependencies (Flask, gunicorn, scikit-learn, numpy, pandas)
│
├── templates/
│   └── index.html          # Responsive frontend UI with Jinja2 templating
│
└── .gitignore
```

---

## 🔢 Input Features

The model takes **8 student metrics** as input:

| Feature | Description | Example |
|---|---|---|
| `IQ` | Intelligence Quotient score | 110 |
| `Prev_Sem_Result` | Previous semester GPA/score | 7.91 |
| `CGPA` | Cumulative Grade Point Average | 8.5 |
| `Academic_Performance` | Overall academic performance rating | 9 |
| `Internship_Experience` | Has internship? (0 = No, 1 = Yes) | 1 |
| `Extra_Curricular_Score` | Score representing activity participation | 5 |
| `Communication_Skills` | Communication skills score | 10 |
| `Projects_Completed` | Number of academic/personal projects | 4 |

---

## 🤖 ML Model

- **Algorithm:** Trained using `scikit-learn` (classification model)
- **Serialization:** Saved using Python `pickle` as `model.pkl`
- **Prediction Output:** Binary — `Placed` (1) or `Not Placed` (0)
- **Input:** `numpy` array of 8 features from form submission

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **ML** | scikit-learn, numpy, pandas |
| **Frontend** | HTML5, CSS3 (inline), Jinja2 templating, Font Awesome |
| **Server** | Gunicorn (production WSGI server) |
| **Deployment** | Render (cloud platform) |

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/your-username/Render-ML.git
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
| `POST` | `/predict` | Accepts form data, runs ML model, returns prediction |

---

## 📊 Key Design Decisions

- **`os.path` for model loading** — Ensures the `model.pkl` path resolves correctly regardless of where the app is run from, critical for cloud deployment.
- **Jinja2 conditional rendering** — The prediction result and status badge are conditionally rendered using `{% if prediction_text %}`, ensuring a clean UI on first load.
- **Gunicorn in requirements** — Production-grade WSGI server explicitly pinned for Render compatibility.

---

## 🔮 Future Improvements

- [ ] Add model accuracy/confidence score to the prediction output
- [ ] Integrate a proper dataset with model retraining pipeline
- [ ] Add input validation with user-friendly error messages
- [ ] Include model explainability (SHAP values) for each prediction
- [ ] Switch from pickle to joblib for safer model serialization
- [ ] Add a REST API endpoint returning JSON (for mobile/API consumers)

---

## 👤 Author

**Nithin Kumar Bonu**
- GitHub: [@bonunithinkumar](https://github.com/bonunithinkumar)
- Deployed via: [Render](https://render.com)

---

*© 2025 Placement Insight's • Data Intelligence Unit*
