from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Machine Type
        machine_type = request.form["type"]

        # Same encoding used during training
        type_mapping = {
            "H": 0,
            "L": 1,
            "M": 2
        }

        machine_type = type_mapping[machine_type]

        # Numerical inputs
        air_temperature = float(request.form["air_temperature"])
        process_temperature = float(request.form["process_temperature"])
        rotational_speed = float(request.form["rotational_speed"])
        torque = float(request.form["torque"])
        tool_wear = float(request.form["tool_wear"])

        # Five numerical features
        numerical_data = np.array([[
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear
        ]])

        # Scale numerical features
        scaled_data = scaler.transform(numerical_data)

        # Final 6 features
        final_data = np.array([[
            machine_type,
            scaled_data[0][0],
            scaled_data[0][1],
            scaled_data[0][2],
            scaled_data[0][3],
            scaled_data[0][4]
        ]])

        # Prediction
        prediction = int(model.predict(final_data)[0])

        if prediction == 1:

            result = "Machine Failure Predicted"
            status = "danger"

            suggestions = [
                "Inspect the machine before continuing operation.",
                "Check the machine temperature and torque conditions.",
                "Inspect the tool for excessive wear.",
                "Check rotating components and lubrication.",
                "Schedule preventive maintenance before normal operation."
            ]

        else:

            result = "No Machine Failure Predicted"
            status = "safe"

            suggestions = [
                "Machine can continue normal operation.",
                "Continue monitoring machine parameters.",
                "Keep checking tool wear regularly.",
                "Follow the scheduled maintenance plan."
            ]

        return render_template(
            "index.html",
            result=result,
            status=status,
            suggestions=suggestions
        )

    except Exception as e:

        return render_template(
            "index.html",
            error="Please enter valid values in all fields."
        )


if __name__ == "__main__":
    app.run(debug=True)