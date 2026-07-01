# 🎬 Movie Recommendation System :-

This is a personal project where I built a highly accurate Movie Recommendation Engine. The core highlight of this project is that the machine learning model was developed and trained entirely from scratch—from rigorous data preprocessing to hyperparameter tuning—rather than just plugging in a pre-made solution.

To showcase software engineering flexibility, I deployed the exact same high-accuracy model using two completely distinct frontend/backend architectural approaches.

---

## 🧠 Core ML Engine & Data Pipeline
* *Jupyter Notebook*: Movie Recommendation Training.ipynb
* *Data Engineering*: Used the TMDB 5000 movies dataset. Handled data cleaning, text preprocessing, missing value imputation, and feature engineering manually.
* *Algorithm*: Implemented Vectorization and Cosine Similarity to calculate distances between movies, ensuring highly precise and contextual recommendation accuracy.

### 🚨 Crucial Setup Note (Download similarity.pkl)
The generated recommendation matrix file (similarity.pkl) is around 176 MB, which exceeds GitHub's direct web upload limits. To run either of the applications locally on your machine, you *must download* this file from my Google Drive and place it inside the respective project directory:

👉 *[Download similarity.pkl from Google Drive](https://drive.google.com/file/d/13BQ1gyEIF_inAo3h26yFmHT0hU1M2quu/view?usp=sharing)*

---

## 📂 Project Architectures

The project is structured into two separate implementations depending on the design preference and workflow complexity:

### 1. Minimalist App (/01-Scratch-Built-Version)
* *Focus*: Pure logic, custom implementation, and lightweight design.
* *Overview*: Built completely with vanilla code for both the frontend and backend configurations. It is designed to be highly readable, focusing purely on the underlying core ML application logic and data workflow without external ecosystem dependencies.

### 2. Production-Ready App (/02-Advanced-UI-Version)
* *Focus*: Premium UI/UX, responsive layouts, and modern architecture.
* *Overview*: Utilizes the exact same custom ML model, but wraps it inside a stunning, highly immersive, and responsive interface powered by the Antigravity framework ecosystem. It mimics a true production-grade commercial application.

---

## 🛠️ Tech Stack Used
* *Machine Learning & Analytics*: Python, Pandas, NumPy, Scikit-Learn, Jupyter Notebook
* *Frameworks & UI Components*: Antigravity UI Framework Ecosystem, Custom Python Scripts
