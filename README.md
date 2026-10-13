# 📱 Smartphone Addiction Prediction Using Machine Learning

A Machine Learning-based web application that predicts smartphone addiction using a trained model and a simple, user-friendly web interface.

## 🌟 About the Project

Smartphones have become an essential part of everyday life. However, excessive smartphone usage may affect sleep, concentration, productivity, and daily routines.

The **Smartphone Addiction Prediction System** aims to demonstrate how Machine Learning can be used to analyze relevant user information and predict smartphone addiction-related outcomes.

The project combines a trained Machine Learning model with a Flask web application, allowing users to interact with the system through a web interface.

## 🎯 Objectives

- Build a Machine Learning model for smartphone addiction prediction.
- Explore the application of data-driven methods to smartphone usage behavior.
- Integrate the trained model into a Flask web application.
- Provide a simple and accessible interface for generating predictions.
- Demonstrate the practical use of Python and Machine Learning in a real-world problem.

## ✨ Key Features

- 🤖 **Machine Learning Prediction** — Uses a saved model to generate predictions.
- 🌐 **Web-Based Application** — Access the prediction interface through a web browser.
- 🐍 **Python Backend** — Uses Python and Flask to handle application logic.
- 🎨 **User Interface** — Provides an interface using HTML templates.
- ⚡ **Pre-trained Model** — Loads the saved model instead of retraining it for every prediction.
- 📊 **Data-Driven Approach** — Applies Machine Learning to a behavioral prediction problem.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and Machine Learning |
| Flask | Web application backend |
| Scikit-learn | Machine Learning model support, if used in training |
| HTML | Web interface structure |
| CSS | Interface styling |
| Pickle | Storage of the trained model |
| GitHub | Source code management and collaboration |

## 🧠 How It Works

1. **Input:** The user provides the information requested by the web interface.
2. **Processing:** Flask receives the submitted information.
3. **Prediction:** The saved Machine Learning model processes the input.
4. **Output:** The application displays the model's prediction to the user.

```text
User Input
    |
    v
Flask Web Application
    |
    v
Input Processing
    |
    v
Trained ML Model
    |
    v
Prediction Result
    |
    v
Result Displayed to User
```

## 📂 Project Structure

```text
smartphone-addiction-prediction/
│
├── app.py
├── smartphone_addiction_model.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── HTML template files
```

**Main files:**

- `app.py` — Main Flask application.
- `smartphone_addiction_model.pkl` — Saved Machine Learning model.
- `requirements.txt` — Python dependencies required by the project.
- `templates/` — HTML templates used to render the web interface.
- `README.md` — Project documentation.

## 🚀 Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python installed on your computer.
- Git installed on your computer.
- A code editor such as Visual Studio Code.

### 1. Clone the Repository

```bash
git clone https://github.com/suryabala-k/smartphone-addiction-prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd smartphone-addiction-prediction
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open the Web Application

Open the local address displayed in your terminal. For a typical Flask development setup, this is:

`http://127.0.0.1:5000/`

Ensure that the saved model file is available at the location expected by `app.py`.

## 📈 Model Information

The application uses a previously trained Machine Learning model stored in `smartphone_addiction_model.pkl`.

The model is loaded by the application to generate predictions from user inputs.

**Model details to document:**
- Algorithm used: To be confirmed from the training code.
- Dataset: Add the dataset name and source.
- Evaluation metrics: Add the actual results from model testing.
- Target variable: Specify the exact prediction label used during training.

## 🔮 Future Enhancements

- Improve model performance through experimentation with different algorithms.
- Add interactive visualizations of smartphone usage patterns.
- Enhance the web interface for mobile devices.
- Provide educational suggestions for maintaining balanced smartphone usage.
- Deploy the application online for easier access.
- Add further evaluation and explainability features.

## ⚠️ Disclaimer

This project is intended for educational and research purposes. Its predictions are based on a Machine Learning model and should not be treated as a medical or psychological diagnosis.

## 👩‍💻 Project Details

**Project Name:** Smartphone Addiction Prediction Using Machine Learning

**Domain:** Artificial Intelligence and Data Science

**Application:** Flask Web Application

**Repository:** [GitHub – Smartphone Addiction Prediction](https://github.com/suryabala-k/smartphone-addiction-prediction)

---

⭐ If you find this project interesting, consider starring the repository!

Contributions, suggestions, and feedback are welcome.

