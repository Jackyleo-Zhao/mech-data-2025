"""Question 2: compute the skewness of each bearing condition."""

from common.influx_config import CONDITIONS
from common.influx_helpers import fetch_stats_for_measurements


def main() -> None:
    stats = fetch_stats_for_measurements(CONDITIONS)
    print("Bearing condition skewness analysis")
    print("-" * 48)
    for condition in CONDITIONS:
        print(f"{condition:<8s} skew = {stats[condition]['skew']:.6f}")


if __name__ == "__main__":
    main()
