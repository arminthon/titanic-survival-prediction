# 🚢 Titanic Survival Prediction & Interactive Web App

[English](#english) | [فارسی](#persian)

---

<a name="english"></a>
## 🇬🇧 English

An end-to-end Machine Learning project using the classic Titanic dataset. The application predicts a passenger's survival probability using an ensemble **Random Forest Classifier** model served through an interactive **Streamlit** dashboard.

### 🌐 Live Demo
Experience the interactive app deployed live on Streamlit Cloud:  
👉 **[titanic-survival-armin.streamlit.app](https://titanic-survival-armin.streamlit.app/)**

### 📌 Features
- **Exploratory Data Analysis (EDA):** Analyzed key passenger attributes (passenger class, age, gender, ticket fare, and family relationships).
- **Data Preprocessing & Cleaning:** Handled missing age values with mean imputation, dropped redundant cabin records, and encoded categorical features.
- **Machine Learning Modeling:**
  - Evaluated baseline models vs. ensemble learning.
  - Upgraded from a simple Decision Tree to a **Random Forest Classifier** (`n_estimators=100`, `max_depth=5`) to improve generalization and deliver realistic survival probabilities.
  - Model serialized via `joblib`.
- **Interactive UI:** Built with Streamlit, enabling intuitive input tuning (sliders, select boxes) and real-time survival probability visualization.

### 🛠️ Tech Stack
- **Python 3**
- **Data Manipulation:** `pandas`, `numpy`
- **Machine Learning:** `scikit-learn`, `joblib`
- **Deployment & UI:** `streamlit`

### 🚀 Local Setup & Run
1. Clone the repository:
```bash
   git clone https://github.com/arminthon/titanic-survival-prediction.git
   cd titanic-survival-prediction
   
