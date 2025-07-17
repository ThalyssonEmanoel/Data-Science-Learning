
# Data-Science-Learning

> This repository contains examples of Machine Learning applications using FastAPI, Streamlit, and Jupyter Notebook, with the penguins dataset.

## How to run the code in this project

### 1. Environment setup

1. Make sure you have **Python 3** installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Training the model (optional)

The `modelo.ipynb` notebook shows how to train the model and save the `model.pkl` and `encoder.pkl` files. Run the notebook if you want to retrain the model.

### 3. Running the API (FastAPI)

1. Start the API by running:
   ```bash
   uvicorn api:app --reload
   ```
2. The API will be available at `http://127.0.0.1:8000`.
3. You can test the `/predict` endpoint using Swagger at `http://127.0.0.1:8000/docs`.

### 4. Running the interface (Streamlit)

1. Run the Streamlit app:
   ```bash
   streamlit run interface.py
   ```
2. Fill in the data in the sidebar and click "Predict species". The app will communicate with the API to return the predicted species.

### 5. Running the notebook

Open the `modelo.ipynb` file in a Jupyter environment (VS Code, JupyterLab, etc.) to see the model training process.

---

**Main files summary:**
- `api.py`: FastAPI API for penguin species prediction.
- `interface.py`: Streamlit web interface for interacting with the model.
- `modelo.ipynb`: Model training notebook.
- `model.pkl` and `encoder.pkl`: Saved model and encoder files.

---
If you have any questions, check the comments in the files or open an issue.
