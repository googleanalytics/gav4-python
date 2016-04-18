# GAV4 Tests [![Analytics](https://ga-beacon.appspot.com/UA-76561751-1/googleanalytics/gav4-python/tests?pixel)](https://github.com/googleanalytics/gav4-python)

## Testing

Run the tests with the following command:

    python setup.py tests

This may require you to install the nose library -- `pip install nose`.

## Contents

### [data.py](data.py)

The `data.py` file contain requests requests, converted requests, responses, converted responses, and mocks of the service objects and its member objects.

### [test_gav4.py](test_gav4.py)

The `test_gav4.py` file contains tests for the gav4 library. It includes unit tests for the individual conversion methods as well as an end-to-end integration test.
