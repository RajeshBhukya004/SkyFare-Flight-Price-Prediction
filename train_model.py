import pandas as pd
import numpy as np
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load the dataset
df = pd.read_csv("data/flight_price.csv")

# 2. Remove unnecessary index columns, if present
df = df.loc[:, ~df.columns.str.contains(r"^Unnamed")]

# 3. Remove rows without a price
df = df.dropna(subset=["price"])

# 4. Separate input features and target
# Flight number is excluded to avoid learning from flight IDs.
X = df.drop(columns=["price", "flight"], errors="ignore")
y = df["price"]

# 5. Identify categorical and numerical columns
categorical_columns = X.select_dtypes(
    include=["object", "category"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    include=["number"]
).columns.tolist()

# 6. Prepare categorical data for machine learning
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns,
        ),
        ("numerical", "passthrough", numerical_columns),
    ]
)

# 7. Create the model pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=15,
                max_depth=15,
                random_state=42,
                min_samples_leaf=5,
                n_jobs=-1,
            ),
        ),
    ]
)

# 8. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training the model. Please wait...")

# 9. Train the model
model.fit(X_train, y_train)

# 10. Evaluate the model on unseen test data
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation")
print("----------------")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r2:.4f}")

# 11. Save the complete pipeline
Path("models").mkdir(exist_ok=True)

joblib.dump(model, "models/flight_price_model.pkl")

print("\nModel saved to models/flight_price_model.pkl")
