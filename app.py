
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

# --------------------------------------------------
# 1. Initialize SkyFare
# --------------------------------------------------

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "flight_price_model.pkl"


# --------------------------------------------------
# 2. Load the trained machine-learning model
# --------------------------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "Trained model not found. "
        "Please run train_model.py first."
    )

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# 3. List the airlines available in our dataset
# --------------------------------------------------

AIRLINES = [
    "Air_India",
    "AirAsia",
    "GO_FIRST",
    "Indigo",
    "SpiceJet",
    "Vistara",
]


# --------------------------------------------------
# 4. Display the homepage
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# 5. Predict prices for multiple airlines
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Read the flight details submitted by the user
        airline = request.form["airline"].strip()
        source_city = request.form["source_city"].strip()
        destination_city = request.form["destination_city"].strip()
        departure_time = request.form["departure_time"].strip()
        arrival_time = request.form["arrival_time"].strip()
        stops = request.form["stops"].strip()
        travel_class = request.form["travel_class"].strip()

        duration = float(request.form["duration"])
        days_left = int(request.form["days_left"])

        # Validate the input
        if source_city == destination_city:
            return render_template(
                "index.html",
                error="Please select two different cities."
            ), 400

        if not 0.5 <= duration <= 50:
            raise ValueError(
                "Duration must be between 0.5 and 50 hours."
            )

        if not 1 <= days_left <= 49:
            raise ValueError(
                "Days until departure must be between 1 and 49."
            )

        if airline not in AIRLINES:
            raise ValueError("Please select a valid airline.")

        # Keep the same feature names and order used during training.
        # The flight-number column was excluded in train_model.py.
        flight_data = {
            "airline": airline,
            "source_city": source_city,
            "departure_time": departure_time,
            "stops": stops,
            "arrival_time": arrival_time,
            "destination_city": destination_city,
            "class": travel_class,
            "duration": duration,
            "days_left": days_left,
        }

        # Generate an estimate for each airline
        flight_options = []

        for option_airline in AIRLINES:

            # Copy the journey details and change the airline
            option_data = flight_data.copy()
            option_data["airline"] = option_airline

            # Convert the details into model input
            input_data = pd.DataFrame([option_data])

            # Predict the estimated fare
            estimated_price = float(
                model.predict(input_data)[0]
            )

            # Save this option for the results page
            flight_options.append({
                "airline": option_airline.replace("_", " "),
                "price": round(estimated_price, 2),
                "selected": option_airline == airline,
            })

        # Sort options by price, lowest first
        flight_options.sort(
            key=lambda option: option["price"]
        )

        # Send the results and journey details to the webpage
        return render_template(
            "index.html",
            flight_details=flight_data,
            flight_options=flight_options,
        )

    except (ValueError, KeyError) as error:
        return render_template(
            "index.html",
            error=str(error),
        ), 400

    except Exception:
        app.logger.exception("Flight price prediction failed")

        return render_template(
            "index.html",
            error=(
                "Unable to predict flight prices. "
                "Please check the model and try again."
            ),
        ), 500


# --------------------------------------------------
# 6. Start the local web server
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
