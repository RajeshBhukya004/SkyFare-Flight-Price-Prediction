# ✈️ SkyFare – Flight Price Prediction

SkyFare is a machine learning-based web application that estimates flight ticket prices based on travel details such as airline, source city, destination city, departure time, number of stops, travel class, flight duration, and days remaining before departure.

The project combines a Python machine learning model with a Flask web application and a modern, user-friendly interface.

## 🚀 Features

- **Flight Price Prediction:** Estimate flight ticket prices using a trained machine learning model.
- **Multiple Airlines:** Compare estimated prices across supported airlines.
- **Route Selection:** Select source and destination cities.
- **Flexible Travel Details:** Enter departure time, arrival time, number of stops, and flight duration.
- **Travel Class Selection:** Choose the required travel class.
- **Advance Booking Analysis:** Include the number of days remaining before departure.
- **Price Sorting:** Sort estimated flight prices from lowest to highest or highest to lowest.
- **Airline Filtering:** Filter results by airline.
- **Responsive Interface:** Access the website through a modern web interface.

> **Note:** SkyFare provides machine learning estimates, not live airline fares. Prices are not real-time booking prices and may differ from actual ticket prices.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web application and routing |
| Pandas | Data handling and preprocessing |
| Scikit-learn | Machine learning pipeline and prediction |
| Joblib | Saving and loading the trained model |
| HTML5 | Website structure |
| CSS3 | Website styling and responsive layout |
| JavaScript | Form interactions, sorting, and filtering |

## 🧠 Machine Learning

SkyFare uses a trained regression model to estimate flight prices.

The model processes travel-related features, including:

- Airline
- Source and destination cities
- Departure and arrival times
- Number of stops
- Travel class
- Flight duration
- Days remaining before departure

Categorical features are encoded through the machine learning preprocessing pipeline before the model generates a price estimate.

The trained model is stored in:

`models/flight_price_model.pkl`

## 📂 Project Structure

```text
Flight-Price-Prediction/
│
├── models/
│   └── flight_price_model.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── explore_data.py
├── requirements.txt
├── README.md
└── .gitignore
```

The dataset and Python virtual environment are excluded from Git tracking.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RajeshBhukya004/SkyFare-Flight-Price-Prediction.git
```

### 2. Open the project directory

```bash
cd SkyFare-Flight-Price-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Prepare the dataset if retraining

Download the flight price dataset used by the training script and place the CSV file at the path expected by that script, such as:

`data/flight_price.csv`

The dataset is not included in this repository.

### 6. Train the model if needed

```bash
python train_model.py
```

Run this step if the trained model file is missing or you want to retrain it. Confirm that the script saves the model to `models/flight_price_model.pkl`.

### 7. Start the web application

```bash
python app.py
```

### 8. Open SkyFare

Visit the following address in your browser:

**http://127.0.0.1:5000**

You can now enter flight details and view estimated prices.

## 📊 Application Workflow

1. The user enters the required travel details.
2. The Flask application receives the submitted form.
3. The application validates the inputs.
4. The trained machine learning pipeline processes the flight details.
5. The model predicts an estimated ticket price for each supported airline.
6. The website displays the estimated prices for comparison.
7. The user can sort and filter the displayed options.

## 🔮 Future Enhancements

- Integrate a legitimate live flight pricing API.
- Add departure dates and more detailed booking information.
- Improve prediction accuracy through model evaluation and tuning.
- Add interactive price comparison charts.
- Include model evaluation metrics such as MAE, RMSE, and R².
- Deploy the application to a cloud hosting platform.
- Add user accounts and saved searches.

## 🎯 Project Objective

The objective of SkyFare is to demonstrate how machine learning can be integrated into a web application to estimate flight ticket prices and help users compare possible travel costs.

## 👨‍💻 Author

**Rajesh Bhukya**

GitHub: [RajeshBhukya004](https://github.com/RajeshBhukya004)

## 📌 Disclaimer

SkyFare is an educational machine learning project. The predicted prices are estimates and should not be treated as guaranteed fares, live airline quotations, or confirmed booking prices.
