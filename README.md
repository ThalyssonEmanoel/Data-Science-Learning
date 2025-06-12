# Data-Science-Learning

This repository contains a Streamlit application for Titanic data analysis with the following features:

## How to Run this Application

1. Make sure you have **Python 3** installed on your machine.
2. Create a virtual environment:
   ```bash
   python -m venv venv or python3 -m venv venvv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
        - On linux:
     ```bash
     source venv/bin/activate
     ```
4. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

## 1. Data Overview

- Displays the total number of passengers.
- Shows the overall survival rate (% survived and % not survived).
- Presents the amount and percentage of missing data in each column.

## 2. Required Visual Analyses

- Bar chart showing survival rate by sex.
- Bar chart of age vs survival.
- Bar chart of survival by ticket class (Pclass).
- Bar chart combining two variables (e.g., sex + class).

## 3. Interactive Filters (Sidebar)

- Allows filtering by:
  - Sex (male/female)
  - Class (1st, 2nd, 3rd)
  - Survivors / non-survivors

## 4. Highlight Missing Data

- Shows which columns have missing data and quantifies it.
- Visualizes how missing data may affect the analysis.

All visualizations are implemented using Plotly and the dashboard is fully interactive.





isso tudo estava no meu git, só mudei pra usar nesse projeto