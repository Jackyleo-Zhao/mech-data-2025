"""InfluxDB connection settings used in the competition environment.

Note:
    These values are kept consistent with the original competition scripts.
    The corresponding tasks require access to the competition-provided
    InfluxDB service in the intranet environment.
"""

TOKEN = "8Ll2EEQOlUGZ6nu2mCtvhQgNfhAzpA9VldCml7evhrG69ZdzlxSyKg6sLiI6H73Mhq8d4_xrhu5wU3zbAHd9bg=="
ORG = "CIMIC"
URL = "http://192.168.124.200:8086"
BUCKET = "maintenance"
DEFAULT_RANGE = "-30d"
CONDITIONS = ["normal", "inner", "outer", "holder"]
UNKNOWN_CONDITION = "unknown"
