"""Question 6: train a random forest model and predict maintenance labels."""

from __future__ import annotations

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from common.paths import DATA_DIR, RESULTS_DIR


TRAIN_DATA_PATH = DATA_DIR / "problem4" / "train.csv"
PREDICT_DATA_PATH = DATA_DIR / "problem4" / "predict.csv"
PREDICTION_OUTPUT_PATH = RESULTS_DIR / "q6_maintenance_predictions.csv"
METRICS_OUTPUT_PATH = RESULTS_DIR / "q6_test_metrics.txt"
FEATURE_OUTPUT_PATH = RESULTS_DIR / "q6_feature_importance.csv"



def load_problem4_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df = pd.read_csv(TRAIN_DATA_PATH)
    predict_df = pd.read_csv(PREDICT_DATA_PATH)
    return train_df, predict_df



def prepare_train_test_split(train_df: pd.DataFrame):
    feature_columns = [
        "temperature",
        "vibration",
        "humidity",
        "pressure",
        "energy_consumption",
    ]
    x = train_df[feature_columns]
    y = train_df["maintenance_required"]
    return train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)



def train_model(x_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(x_train, y_train)
    return model



def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    train_df, predict_df = load_problem4_data()

    x_train, x_test, y_train, y_test = prepare_train_test_split(train_df)
    model = train_model(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, digits=4)

    prediction_features = predict_df.drop(columns=["id"])
    maintenance_prediction = model.predict(prediction_features)

    prediction_result = pd.DataFrame(
        {
            "id": predict_df["id"],
            "maintenance_required": maintenance_prediction,
        }
    )
    prediction_result.to_csv(PREDICTION_OUTPUT_PATH, index=False, encoding="utf-8-sig")

    feature_importance = pd.DataFrame(
        {
            "feature": x_train.columns,
            "importance": model.feature_importances_,
        }
    ).sort_values(by="importance", ascending=False)
    feature_importance.to_csv(FEATURE_OUTPUT_PATH, index=False, encoding="utf-8-sig")

    with open(METRICS_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(f"Test accuracy: {accuracy:.4f}\n\n")
        file.write("Classification report:\n")
        file.write(report)

    print("Maintenance prediction completed.")
    print(f"Test accuracy: {accuracy:.4f}")
    print(f"Predictions saved to: {PREDICTION_OUTPUT_PATH}")
    print(f"Metrics saved to: {METRICS_OUTPUT_PATH}")
    print(f"Feature importance saved to: {FEATURE_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
