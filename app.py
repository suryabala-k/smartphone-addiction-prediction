from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load the trained machine learning model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "smartphone_addiction_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error_message = None
    form_data = {}

    if request.method == "POST":
        try:
            age = int(request.form["age"])
            gender = request.form["gender"]
            daily_usage = float(request.form["daily_usage"])
            sleep_hours = float(request.form["sleep_hours"])
            academic_performance = float(
                request.form["academic_performance"]
            )
            phone_checks = int(request.form["phone_checks"])
            apps_used = int(request.form["apps_used"])
            social_media = float(request.form["social_media"])
            gaming = float(request.form["gaming"])

            form_data = request.form.to_dict()

            # Validate input values
            if not 10 <= age <= 100:
                raise ValueError("Age must be between 10 and 100.")

            if not 0 <= daily_usage <= 24:
                raise ValueError(
                    "Daily usage must be between 0 and 24 hours."
                )

            if not 0 <= sleep_hours <= 24:
                raise ValueError(
                    "Sleep duration must be between 0 and 24 hours."
                )

            if not 0 <= social_media <= 24:
                raise ValueError(
                    "Social media usage must be between 0 and 24 hours."
                )

            if not 0 <= gaming <= 24:
                raise ValueError(
                    "Gaming time must be between 0 and 24 hours."
                )

            if phone_checks < 0 or apps_used < 0:
                raise ValueError(
                    "Phone checks and apps used cannot be negative."
                )

            # Prepare input using the exact feature names
            input_data = pd.DataFrame([{
                "Age": age,
                "Gender": gender,
                "Daily_Usage_Hours": daily_usage,
                "Sleep_Hours": sleep_hours,
                "Academic_Performance": academic_performance,
                "Phone_Checks_Per_Day": phone_checks,
                "Apps_Used_Daily": apps_used,
                "Time_on_Social_Media": social_media,
                "Time_on_Gaming": gaming
            }])

            # Generate prediction
            prediction = model.predict(input_data)[0]

        except ValueError as error:
            error_message = str(error)

        except Exception:
            error_message = (
                "Prediction failed. Please check the model "
                "and the input feature formats."
            )

    return render_template(
        "index.html",
        prediction=prediction,
        error_message=error_message,
        form_data=form_data
    )


if __name__ == "__main__":
    app.run(debug=True)
