"""Question 4: compute the standard deviation and skewness of unknown condition."""

from common.influx_config import UNKNOWN_CONDITION
from common.influx_helpers import fetch_stats_for_measurements


def main() -> None:
    stats = fetch_stats_for_measurements([UNKNOWN_CONDITION])
    unknown_stats = stats[UNKNOWN_CONDITION]

    print("Unknown condition statistics")
    print("-" * 48)
    print(f"std  = {unknown_stats['std']:.6f}")
    print(f"skew = {unknown_stats['skew']:.6f}")


if __name__ == "__main__":
    main()
