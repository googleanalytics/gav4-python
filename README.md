# Google Analytics V4 Compatibility Library

Library for converting V3 API request to v4 API requests.

## Quick Start

    $ pip install --upgrade gav4


## Typical usage example

There are two methods of using the gav4 libary. The first being you can
`apply` the library to an authorized Google Analytics Service object, which
exposes a get method that operates much like the current v3 Core Reporting
API. Alternatively you can call the conversion methods directly.


    from gcloud import datastore
    import gav4
    gav4.apply_gav4(analytics)

    v3_response = analytics.gav4_get(v3_request).execute()

    # Alternatively you can convert the request directly
    v4_request = gav4.convert_request(v3_request)

    v4_response = analytics.reports().batchGet(body=v4_request).execute()

    v3_response = gav4.convert_report(v4_response.get('reports', [])[0])


## Contributing

Before we can use your code, you must sign the
[Google Individual Contributor License Agreement](https://developers.google.com/open-source/cla/individual?csw=1)
(CLA), which you can do online. The CLA is necessary mainly because you own the
copyright to your changes, even after your contribution becomes part of our
codebase, so we need your permission to use and distribute your code. We also
need to be sure of various other things—for instance that you'll tell us if you
know that your code infringes on other people's patents. You don't have to sign
the CLA until after you've submitted your code for review and a member has
approved it, but you must do it before we can put your code into our codebase.
Before you start working on a larger contribution, you should get in touch with
us first through the issue tracker with your idea so that we can help out and
possibly guide you. Coordinating up front makes it much easier to avoid
frustration later on.

### Code reviews
All submissions, including submissions by project members, require review. We
use Github pull requests for this purpose.

### The small print
Contributions made by corporations are covered by a different agreement than
the one above, the Software Grant and Corporate Contributor License Agreement.
