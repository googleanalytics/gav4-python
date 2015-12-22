#!/usr/bin/env python
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.apputils import basetest as googletest

import gav4_lib
from data import testing


__author__ = 'mcohoon@google.com (Matthew Cohoon)'


class Gav4LibTest(googletest.TestCase):

  def testConvertResponse(self):
    """Test the report conversion."""
    report = testing.V4_RESPONSE.get('reports', [])[0]
    data = gav4_lib.convert_report(report)
    self.assertDictContainsSubset(testing.V3_CONVERTED_RESPONSE, data)

  def testConvertDimensions(self):
    """Test the conversion of Dimensions."""
    dimensions = 'ga:country,ga:browser'
    response = gav4_lib.convert_dimensions(dimensions)
    reference = [{'name': 'ga:country'}, {'name': 'ga:browser'}]
    self.assertItemsEqual(reference, response)

  def testConvertMetrics(self):
    """Test the conversion of metrics."""
    metrics = 'ga:sessions,ga:users'
    response = gav4_lib.convert_metrics(metrics)
    reference = [{'expression': 'ga:sessions'}, {'expression': 'ga:users'}]
    self.assertItemsEqual(reference, response)

  def testConvertSegments(self):
    """Test the conversion of segments."""
    segments = 'users::condition::ga:city==London;ga:browser==Chrome'
    response = gav4_lib.convert_segments(segments)
    reference = [{'segmentExpression': segments}]
    self.assertEquals(response, reference)

  def testConvertOrderings(self):
    """Test the conversion of v3 sorts into v4 orderBys."""
    sort = 'ga:country,-ga:browser,-ga:sessions'
    order_bys = gav4_lib.convert_sorting(sort)
    self.assertItemsEqual(order_bys, testing.ORDER_BYS)

  def testConvertRequest(self):
    """Tests the conversion of a v3 request."""
    response = gav4_lib.convert_request(**testing.V3_REQUEST)
    self.assertDictContainsSubset(response, testing.V4_REQUEST)

  def testGav4Get(self):
    """An end to end integration test of the gav4 library.

    This represents what the end user would do with the gav4 library.
    Given an authenticated service object we apply the gav4, and then
    make a call as if we were still using the v3 library.
    """

    # Get the MOCK authenticated service object.
    analytics = testing.Analytics()

    # Apply the gav4 library.
    gav4_lib.apply_gav4(analytics)

    # Call the veeneer_get() method.
    request = analytics.gav4_get(**testing.V3_REQUEST)

    # Call the wrapped execute method.
    response = request.execute()
    self.assertItemsEqual(response, testing.V3_CONVERTED_RESPONSE)


if __name__ == '__main__':
  googletest.main()
