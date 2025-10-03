# 🚗 Predicting Road Accident Risk  

A complete **end-to-end machine learning project** based on the Kaggle competition  
👉 [Playground Series - Season 5, Episode 10](https://www.kaggle.com/competitions/playground-series-s5e10).  

The goal is to **predict road accident risk** using machine learning techniques with full **MLOps integration**:  
- **XGBoost** for modeling.  
- **DVC** for pipeline tracking.  
- **MLflow** for experiment tracking.  
- **Streamlit** app for interactive model inference.  
- **FastAPI** service for REST API inference.  
- **Docker** for containerization and deployment.  
---

# 🛠️ Tech Stack

- **Machine Learning** : XGBoost, Scikit-learn, Pandas, NumPy

- **MLOps** : DVC, MLflow, Hydra

- **Deployment** : Streamlit, FastAPI, Docker, Uvicorn

- **Visualization** : Matplotlib, Seaborn

# 4️⃣ Setup MLflow tracking
Run MLflow server locally:
```bash
mlflow ui --port 5000
```

# 🖥️ Streamlit App
Run the interactive web app for predictions:
```bash
streamlit run main.py
```

# ⚡ FastAPI Service
Run the FastAPI app for REST inference:
```bash
uvicorn app:app --port 8000
```

# ✨ Future Improvements

 - **CI/CD** : GitHub Actions.

