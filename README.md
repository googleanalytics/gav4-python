# Google Analytics Reporting V4 Compatibility Library

A library for converting Google Analytics Core Reporting API V3 request to Analytics Reporting API V4 requests.

## Installation

    $ pip install --upgrade gav4


## Typical usage example

There are two methods of using the gav4 library. You can `apply` the library to an authorized Google Analytics Service object, which exposes a get method that operates much like the current Core Reporting API V3.

    import gav4

    # Apply the gav4 get method to the authorized service object.
    gav4.apply_gav4(analytics)

    # Call the gav4_get method with a V3 request and get a V3 response.
    v3_response = analytics.gav4_get(v3_request).execute()

Alternatively you can convert the requests and responses directly.

    # Convert a V3 request into a V4 request.
    v4_request = gav4.convert_request(v3_request)

    # Call the V4 API.
    v4_response = analytics.reports().batchGet(body=v4_request).execute()

    # Convert the V4 API response into a V3 response.
    v3_response = gav4.convert_report(v4_response.get('reports', [])[0])

## Testing

Run the tests with the following command:

    python setup.py tests

This may require you to install the nose library -- `pip install nose`.

## Contributing

1. **Please sign one of the contributor license agreements below.**
2. Fork the repository, develop and test your code changes, add docs.
3. Make sure that your commit messages clearly describe the changes.
4. Send a pull request.


### Contributor License Agreements


Before we can accept your pull requests you'll need to sign a Contributor License Agreement (CLA):

- **If you are an individual writing original source code** and **you own the intellectual property**, then you'll need to sign an [individual CLA](https://developers.google.com/open-source/cla/individual).
- **If you work for a company that wants to allow you to contribute your work**, then you'll need to sign a [corporate CLA](https://developers.google.com/open-source/cla/corporate).

You can sign these electronically (just scroll to the bottom). After that, we'll be able to accept your pull requests.


### Code reviews
All submissions, including submissions by project members, require review. We
use Github pull requests for this purpose.

