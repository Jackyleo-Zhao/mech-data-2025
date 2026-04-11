"""Question 3: visualize the skewness of each bearing condition."""

from pathlib import Path

import matplotlib.pyplot as plt

from common.influx_config import CONDITIONS
from common.influx_helpers import fetch_stats_for_measurements
from common.paths import RESULTS_DIR


def main() -> None:
    stats = fetch_stats_for_measurements(CONDITIONS)
    conditions = CONDITIONS
    skew_values = [stats[condition]["skew"] for condition in conditions]

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RESULTS_DIR / "q3_bearing_skew_bar.png"

    plt.figure(figsize=(8, 5))
    plt.bar(conditions, skew_values)
    plt.xlabel("Bearing condition")
    plt.ylabel("Skewness")
    plt.title("Skewness of different bearing conditions")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Saved figure to: {output_path}")
    plt.show()


if __name__ == "__main__":
    main()
