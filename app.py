import joblib
import pandas as pd
import streamlit as st

# عنوان و توضیحات اپلیکیشن
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢")
st.title("🚢 پیش‌بینی نجات‌یافتگان تایتانیک")
st.write(
    "مشخصات مسافر را وارد کنید تا احتمال نجات یافتن توسط مدل هوش مصنوعی (Random Forest) محاسبه شود."
)

# بارگذاری مدل آموزش‌دیده
model = joblib.load("titanic_model.pkl")

# چیدمان ورودی‌ها در دو ستون
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox(
        "کلاس بلیط (1=لوکس، 2=متوسط، 3=عادی):", [1, 2, 3], index=2
    )
    sex = st.selectbox("جنسیت:", ["زن", "مرد"])
    age = st.slider("سن مسافر:", min_value=1, max_value=80, value=25)

with col2:
    fare = st.slider(
        "قیمت بلیط به دلار ($):", min_value=0, max_value=500, value=30
    )
    sibsp = st.number_input("تعداد همسر یا برادر/خواهر همراه:", 0, 10, 0)
    parch = st.number_input("تعداد والدین یا فرزندان همراه:", 0, 10, 0)

# تبدیل جنسیت به عدد برای مدل
sex_val = 1 if sex == "زن" else 0

# آماده‌سازی داده مسافر برای ارسال به مدل
user_data = pd.DataFrame(
    [[pclass, sex_val, age, fare, sibsp, parch]],
    columns=["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"],
)

st.write("---")

# دکمه اجرای پیش‌بینی
if st.button("🔮 محاسبه شانس بقا", use_container_width=True):
    prediction = model.predict(user_data)[0]
    proba = model.predict_proba(user_data)[0][1] * 100

    st.write(f"### احتمال زنده ماندن: **{proba:.1f}%**")

    # نوار پیشرفت درصد
    st.progress(int(proba))

    if prediction == 1:
        st.success(
            "🎉 مدل پیش‌بینی می‌کند این مسافر به احتمال زیاد نجات می‌یافت!"
        )
    else:
        st.error(
            "⚠️ مدل پیش‌بینی می‌کند این مسافر متأسفانه شانس پایینی برای نجات داشت."
        )
