# 🚢 Titanic Survival Prediction with Decision Tree

A machine learning project predicting passenger survival on the Titanic dataset, focusing on exploratory data analysis, data cleaning, and handling **overfitting**.

## 📌 Project Overview
- **Data Preprocessing & Cleaning:** Handled missing values in `Age` and `Embarked`, dropped high-missing column `Cabin`.
- **Feature Engineering:** Encoded categorical features (`Sex`) into numeric format for modeling.
- **Exploratory Data Analysis (EDA):** Visualized survival distributions across passenger classes (`Pclass`) and genders.
- **Modeling:** Built and evaluated a `DecisionTreeClassifier` using Scikit-Learn.
- **Overfitting Prevention:** Tuned `max_depth` to prevent the decision tree from memorizing the training data.

## 📊 Results & Key Takeaways
- **Default Tree (Unconstrained):**
  - Train Accuracy: ~**98.6%** (High Overfitting)
  - Test Accuracy: ~**76.9%**
- **Pruned Tree (`max_depth=3`):**
  - Train Accuracy: **82.2%**
  - Test Accuracy: **82.0%**
  - Result: Eliminates overfitting, achieving balanced and robust generalization on unseen test data.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-Learn
