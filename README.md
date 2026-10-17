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

---

<a name="persian"></a>
<div dir="rtl">

## 🇮🇷 فارسی

یک پروژه یادگیری ماشین از ابتدا تا استقرار نهایی بر روی دیتاست معروف تایتانیک. این برنامه درصد احتمال نجات مسافران را با استفاده از الگوریتم آنسامبل **Random Forest Classifier** تخمین می‌زند و نتیجه را در یک داشبورد تعاملی **Streamlit** نمایش می‌دهد.

### 🌐 مشاهده آنلاین (دموی لایو)
برنامه را به صورت زنده در استریم‌لیت کلاود تست کنید:  
👉 **[titanic-survival-armin.streamlit.app](https://titanic-survival-armin.streamlit.app/)**

### 📌 ویژگی‌های پروژه
- **تحلیل داده‌ها (EDA):** بررسی ویژگی‌های اثرگذار مسافران از جمله طبقه بلیط، سن، جنسیت، کرایه و همراهان خانوادگی.
- **پیش‌پردازش داده‌ها:** مدیریت داده‌های ناموجود سن با مقدار میانگین، حذف ویژگی‌های پر از داده از‌دست‌رفته و کدگذاری متغیرهای دسته‌ای.
- **مدل‌سازی یادگیری ماشین:**
  - آموزش مدل اولیه با درخت تصمیم و ارتقا به مدل ترکیبی **Random Forest Classifier** جهت جلوگیری از اورفیتینگ و ایجاد احتمالات نرم و واقع‌گرایانه.
  - ذخیره‌سازی مدل با استفاده از کتابخانه `joblib`.
- **رابط کاربری تعاملی:** توسعه وب‌اپلیکیشن کاربرپسند با استفاده از Streamlit جهت تغییر آسان پارامترها و مشاهده بلادرنگ نتیجه پیش‌بینی.

### 🛠️ ابزارها و تکنولوژی‌ها
- **زبان:** پایتون (Python 3)
- **پردازش داده:** `pandas` و `numpy`
- **یادگیری ماشین:** `scikit-learn` و `joblib`
- **رابط کاربری و استقرار:** `streamlit`

### 🚀 راه‌اندازی و اجرای محلی
۱. کلون کردن ریپازیتوری:
```bash
git clone https://github.com/arminthon/titanic-survival-prediction.git
cd titanic-survival-prediction
