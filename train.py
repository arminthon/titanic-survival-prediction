import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

print("در حال دریافت داده‌ها...")
url = (
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
titanic = pd.read_csv(url)

# پیش‌پردازش
titanic = titanic.drop(columns=["Cabin"])
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())
titanic = titanic.dropna(subset=["Embarked"])
titanic["Sex"] = titanic["Sex"].map({"female": 1, "male": 0})

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
X = titanic[features]
y = titanic["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ساخت مدل جنگل تصادفی
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# ارزیابی و ذخیره
acc = accuracy_score(y_test, model.predict(X_test))
print(f"دقت مدل جدید (Random Forest): {acc * 100:.2f}%")

joblib.dump(model, "titanic_model.pkl")
print("مدل titanic_model.pkl با موفقیت ذخیره شد!")
