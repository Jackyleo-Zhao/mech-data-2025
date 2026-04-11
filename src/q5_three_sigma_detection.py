"""Question 5: detect abnormal vibration samples using the 3-sigma rule."""

from __future__ import annotations

import pandas as pd

from common.paths import DATA_DIR, RESULTS_DIR


NORMAL_DATA_PATH = DATA_DIR / "problem3" / "normal_reference.csv"
UNKNOWN_DATA_PATH = DATA_DIR / "problem3" / "unknown_samples.csv"
OUTPUT_PATH = RESULTS_DIR / "q5_three_sigma_detection.csv"
SUMMARY_PATH = RESULTS_DIR / "q5_three_sigma_summary.txt"



def load_problem3_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    normal_df = pd.read_csv(NORMAL_DATA_PATH)
    unknown_df = pd.read_csv(UNKNOWN_DATA_PATH)
    return normal_df, unknown_df



def detect_anomalies(normal_df: pd.DataFrame, unknown_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    reference = normal_df["vibration"]
    mean_value = float(reference.mean())
    std_value = float(reference.std(ddof=0))
    lower_bound = mean_value - 3 * std_value
    upper_bound = mean_value + 3 * std_value

    result_df = unknown_df.copy()
    result_df["mean_reference"] = mean_value
    result_df["std_reference"] = std_value
    result_df["lower_bound"] = lower_bound
    result_df["upper_bound"] = upper_bound
    result_df["is_anomaly"] = (
        (result_df["vibration"] < lower_bound) | (result_df["vibration"] > upper_bound)
    )

    summary = {
        "mean": mean_value,
        "std": std_value,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "num_samples": int(len(result_df)),
        "num_anomalies": int(result_df["is_anomaly"].sum()),
    }
    return result_df, summary



def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    normal_df, unknown_df = load_problem3_data()
    result_df, summary = detect_anomalies(normal_df, unknown_df)

    result_df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
    with open(SUMMARY_PATH, "w", encoding="utf-8") as file:
        file.write("Three-sigma anomaly detection summary\n")
        file.write("-" * 40 + "\n")
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

    print("Three-sigma anomaly detection completed.")
    print(f"Results saved to: {OUTPUT_PATH}")
    print(f"Summary saved to: {SUMMARY_PATH}")
    print(result_df)


if __name__ == "__main__":
    main()
