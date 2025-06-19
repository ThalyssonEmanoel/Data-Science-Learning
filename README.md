# Data-Science-Learning

This repository contains a practical example of machine learning using Python and scikit-learn to predict student performance based on study data.

## How to Run This Project

1. Make sure you have **Python 3** installed on your machine.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install pandas scikit-learn seaborn
   ```
5. Open and run the `main.ipynb` notebook in your preferred editor (VS Code, Jupyter Notebook, etc).

## 1. Dataset Overview

- The dataset `student_performance.csv` includes:
  - `horas_estudo`: Number of study hours.
  - `nota_provas`: Exam scores.
  - `presenca (%)`: Attendance percentage.
  - `passou`: 1 if the student passed, 0 otherwise.

## 2. Analysis Workflow

- Load the CSV file using pandas.
- Select predictor variables (`horas_estudo`, `nota_provas`, `presenca (%)`) and the target variable (`passou`).
- Split the data into training and test sets.
- Train a Decision Tree Classifier.
- Evaluate the model using accuracy and confusion matrix.

## 3. Results

- The notebook displays:
  - The accuracy of the trained model.
  - The confusion matrix showing classification performance.

## 4. Visualization

- The code can be easily extended to include visualizations and exploratory analysis using seaborn or matplotlib.

---

Feel free to modify the notebook and experiment with other algorithms or analyses!