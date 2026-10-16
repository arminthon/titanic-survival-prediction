url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)

titanic.head()
titanic.isnull().sum()
titanic = titanic.drop(columns=["Cabin"])
titanic.isnull().sum()
mean_age = titanic["Age"].mean()
titanic["Age"] = titanic["Age"].fillna(mean_age)
titanic.isnull().sum()
titanic = titanic.dropna(subset=["Embarked"])
titanic.isnull().sum()
titanic.groupby("Sex")["Survived"].mean()
titanic.groupby("Pclass")["Survived"].mean()
titanic.groupby(["Pclass", "Sex"])["Survived"].mean().plot(kind="bar")
titanic["Sex"] = titanic["Sex"].map({"female": 1, "male": 0})
titanic.head()
features = ["Pclass", "Sex", "Age", "Fare"]
X = titanic[features]
y = titanic["Survived"]
X.head()
y.head()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("تعداد داده‌های آموزش:", len(X_train))
print("تعداد داده‌های تست:", len(X_test))
print("تعداد کل داده‌ها:", len(titanic))
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
from sklearn.tree import DecisionTreeClassifier

# ۱. ساخت مدل
model = DecisionTreeClassifier()

# ۲. آموزش مدل با داده‌های Train
model.fit(X_train, y_train)

# ۳. پیش‌بینی روی داده‌های Test
predictions = model.predict(X_test)
print(predictions[:10])
# ۱۰ تای اول از داده‌های تست رو کپی می‌کنیم
sample = X_test.head(10).copy()

# ستون پیش‌بینی مدل رو اضافه می‌کنیم
sample["Predicted"] = predictions[:10]

# ستون جواب واقعی رو هم می‌ذاریم کنارش تا مقایسه کنیم!
sample["Actual"] = y_test.head(10).values

sample

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))
X = titanic[["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]]
y = titanic["Survived"]
X.head()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(accuracy_score(y_test, predictions))

# این بار به درخت می‌گیم عمقش بیشتر از 3 نشه
smart_model = DecisionTreeClassifier(max_depth=3)

smart_model.fit(X_train, y_train)

smart_preds = smart_model.predict(X_test)

print(accuracy_score(y_test, smart_preds))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# تنظیم اندازه تصویر که بزرگ و خوانا باشه
plt.figure(figsize=(16, 8))

# کشیدن شکل درخت
plot_tree(
    smart_model,
    feature_names=X.columns,
    class_names=["Died", "Survived"],
    filled=True,
    rounded=True,
)

plt.show()
