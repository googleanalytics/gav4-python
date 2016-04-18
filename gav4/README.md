# Google Analytics Reporting API V4 Compatibility Library [![Analytics](https://ga-beacon.appspot.com/UA-76561751-1/googleanalytics/gav4-python/gav4?pixel)](https://github.com/googleanalytics/gav4-python)

## Contents

### [`gav4.py`](gav4.py)

The `gav4.py` contains functions to convert each of the [Core Reporting API V3](https://developers.google.com/analytics/devguides/reporting/core/v3/) parameters to [Analytics Reporting API V4](https://developers.google.com/analytics/devguides/reporting/core/v4/) request fields.

The file also contains the `apply_gav4` function which can be called with an authorized `analyticsreporting` service object; once applied, you can call:

    `analyticsreporting.gav4_get(...)`

which takes the same parameters and returns the same response as when you call the Core reporting API V3 method:

    `analytics.data().ga().get(...)`
