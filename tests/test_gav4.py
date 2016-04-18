#!/usr/bin/env python
# Copyright 2016 Google Inc. All rights reserved.
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

"""Tests for the gav4 library."""

from google.apputils import basetest as googletest

from gav4 import gav4
from tests import data


__author__ = 'mcohoon@google.com (Matthew Cohoon)'


class Gav4LibTest(googletest.TestCase):

  def testConvertResponse(self):
    """Test the report conversion."""
    report = data.V4_RESPONSE.get('reports', [])[0]
    converted_report = gav4.convert_report(report)
    self.assertDictContainsSubset(data.V3_CONVERTED_RESPONSE, converted_report)

  def testConvertDimensions(self):
    """Test the conversion of Dimensions."""
    dimensions = 'ga:country,ga:browser'
    response = gav4.convert_dimensions(dimensions)
    reference = [{'name': 'ga:country'}, {'name': 'ga:browser'}]
    self.assertItemsEqual(reference, response)

  def testConvertMetrics(self):
    """Test the conversion of metrics."""
    metrics = 'ga:sessions,ga:users'
    response = gav4.convert_metrics(metrics)
    reference = [{'expression': 'ga:sessions'}, {'expression': 'ga:users'}]
    self.assertItemsEqual(reference, response)

  def testConvertSegments(self):
    """Test the conversion of segments."""
    segments = 'users::condition::ga:city==London;ga:browser==Chrome'
    response = gav4.convert_segments(segments)
    reference = [{'segmentId': segments}]
    self.assertEquals(response, reference)

  def testConvertOrderings(self):
    """Test the conversion of V3 sorts into V4 orderBys."""
    sort = 'ga:country,-ga:browser,-ga:sessions'
    order_bys = gav4.convert_sorting(sort)
    self.assertItemsEqual(order_bys, data.ORDER_BYS)

  def testConvertRequest(self):
    """Tests the conversion of a V3 request."""
    response = gav4.convert_request(**data.V3_REQUEST)
    self.assertDictContainsSubset(response, data.V4_REQUEST)

  def testGav4Get(self):
    """An end to end integration test of the gav4 library.

    This represents what the end user would do with the gav4 library.
    Given an authenticated service object, we apply gav4, and then
    make a call as if we were still using the V3 library.
    """

    # Get the MOCK authenticated service object.
    analyticsreporting = data.AnalyticsReporting()

    # Apply the gav4 library.
    gav4.apply_gav4(analyticsreporting)

    # Call the gav4_get() method.
    request = analyticsreporting.gav4_get(**data.V3_REQUEST)

    # Call the wrapped execute method.
    response = request.execute()
    self.assertItemsEqual(response, data.V3_CONVERTED_RESPONSE)


if __name__ == '__main__':
  googletest.main()
