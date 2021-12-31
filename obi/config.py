import os
import pathlib

# Weather API
WX_API_KEY = os.environ.get("WX_API_KEY", "94a85300309e5327e7c06fddef703b67")
WX_LOCATION = os.environ.get("WX_LOCATION", "Cape Town")
WX_METRIC_TEMP = os.environ.get("WX_METRIC_TEMP", "celsius")
WX_METRIC_WIND = os.environ.get("WX_METRIC_WIND", "km_hour")

