"""Utilities for querying InfluxDB and computing basic statistics."""

from __future__ import annotations

from typing import Dict

import influxdb_client
import numpy as np
import pandas as pd

from common.influx_config import BUCKET, DEFAULT_RANGE, ORG, TOKEN, URL


def create_client() -> influxdb_client.InfluxDBClient:
    """Create an InfluxDB client using the original competition settings."""
    return influxdb_client.InfluxDBClient(url=URL, token=TOKEN, org=ORG)


def build_measurement_query(measurement: str, time_range: str = DEFAULT_RANGE) -> str:
    return (
        f'from(bucket: "{BUCKET}")\n'
        f'  |> range(start: {time_range})\n'
        f'  |> filter(fn: (r) => r._measurement == "{measurement}")'
    )


def fetch_measurement_values(client: influxdb_client.InfluxDBClient, measurement: str) -> np.ndarray:
    """Fetch all values for a measurement and return them as a float array."""
    query_api = client.query_api()
    query = build_measurement_query(measurement=measurement)
    tables = query_api.query(query, org=ORG)

    values = []
    for table in tables:
        for record in table.records:
            value = record.get_value()
            if value is not None:
                values.append(float(value))

    if not values:
        raise ValueError(f"No values were returned for measurement: {measurement}")

    return np.asarray(values, dtype=float)


def measurement_stats(values: np.ndarray) -> Dict[str, float]:
    """Compute basic descriptive statistics for one measurement."""
    return {
        "count": int(values.size),
        "mean": float(np.mean(values)),
        "std": float(np.std(values)),
        "skew": float(pd.Series(values).skew()),
        "min": float(np.min(values)),
        "max": float(np.max(values)),
    }


def fetch_stats_for_measurements(measurements: list[str]) -> Dict[str, Dict[str, float]]:
    """Query multiple measurements and compute their statistics."""
    client = create_client()
    try:
        return {
            measurement: measurement_stats(fetch_measurement_values(client, measurement))
            for measurement in measurements
        }
    finally:
        client.close()
