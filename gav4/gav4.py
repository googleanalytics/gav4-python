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

"""Library for converting V3 API request to v4 API requests.

This library contains helper functions to convert a
Google Analytics Core Reporting API request
from a V3 API request into a v4 API Request. It is designed to work in
concert to the Google API Python client library.

  Typical usage example:

  import gav4
  gav4.apply_gav4(analytics)

  v3_response = analytics.gav4_get(v3_request).execute()

  # Alternatively you can convert the request directly
  v4_request = gav4.convert_request(v3_request)

  v4_response = analytics.reports().batchGet(body=v4_request).execute()

  v3_response = gav4.convert_report(v4_response.get('reports', [])[0])

"""

from functools import partial


__author__ = 'mcohoon@google.com (Matthew Cohoon)'

GA_SEGMENT = 'ga:segment'

SAMPLING_MAP = {
    'DEFAULT': 'DEFAULT',
    'FASTER': 'SMALL',
    'HIGHER_PRECESION': 'LARGE'
}


def convert_dimensions(dimensions):
  """Converts v3 dimension parameters into v4 parameters."""
  return [{'name': name} for name in dimensions.split(',')]


def convert_metrics(metrics):
  """Converts v3 metric parameters into v4 parameters."""
  converted_metrics = []
  for expression in metrics.split(','):
    metric = {
        'expression': expression,
    }
    converted_metrics.append(metric)
  return converted_metrics


def convert_segments(segment):
  """Converts the V3 segment string syntax into the v4 syntax."""
  return [{'segmentExpression': segment}]


def convert_sorting(sortings):
  """Convert the V3 orderings into v4 Syntax.

  Args:
    sortings: A string v3 representation of sorting.
  Returns:
    A list of v4 orderBy objects.
  """
  order_bys = []

  for sorting in sortings.split(','):
    order_by = {}
    order_by['orderType'] = 'VALUE'
    if sorting.startswith('-'):
      order_by['fieldName'] = sorting[1:] + ' desc'
    else:
      order_by['fieldName'] = sorting
    order_bys.append(order_by)
  return order_bys


def convert_sampling(sampling):
  """Converts the v3 sampling string into v4 syntax."""
  return SAMPLING_MAP.get(sampling, 'SAMPLING_UNSPECIFIED')


def convert_dateranges(kwargs):
  """Creates the date range object from the parameters dictionary.

  Args:
    kwargs: a dict containing the parameters passed in the request.
  Returns:
    A DateRange object, a dictionary.
  """
  date_range = {
      'startDate': kwargs.get('start_date', None),
      'endDate': kwargs.get('end_date', None)
  }
  return [date_range]


def gav4_execute(self):
  """A method hijack the execute to get the response."""

  # Call the old execute.
  reports = self.old_execute()

  # Convert the response.
  return convert_report(reports.get('reports', [])[0])


def convert_request(**kwargs):
  """Converts the v3 request to a v4 request."""
  report_request = {}

  # Convert the required arguments
  report_request['viewId'] = kwargs.get('ids')
  report_request['dateRanges'] = convert_dateranges(kwargs)
  report_request['metrics'] = convert_metrics(kwargs.get('metrics'))

  if 'dimensions' in kwargs:
    report_request['dimensions'] = convert_dimensions(kwargs.get('dimensions'))

  if 'segment' in kwargs:
    report_request['segments'] = convert_segments(kwargs.get('segment'))

    # Add the 'ga:segment' dimension.
    dimensions = report_request.get('dimensions', [])
    dimensions.append({'name': GA_SEGMENT})
    report_request['dimensions'] = dimensions

  if 'filters' in kwargs:
    report_request['filtersExpression'] = kwargs.get('filters')

  if 'sort' in kwargs:
    report_request['order_bys'] = convert_sorting(kwargs.get('sort'))

  if 'samplingLevel' in kwargs:
    report_request['samplingLevel'] = convert_sampling(
        kwargs.get('samplingLevel'))

  if 'max_results' in kwargs:
    report_request['pageSize'] = kwargs.get('max_results')

  if 'include_empty_rows' in kwargs:
    report_request['includeEmptyRows'] = kwargs.get('include_empty_rows')

  return {'reportRequests': [report_request]}


def gav4_get(self, **kwargs):
  """A service object method this method converts and calls the requests."""
  batch_get = self.reports().batchGet(body=convert_request(**kwargs))

  # Rename the existing batch get so we hijack the response.
  batch_get.old_execute = batch_get.execute
  batch_get.execute = partial(gav4_execute, batch_get)
  return batch_get


def apply_gav4(analytics):
  """Applies the gav4 coating to the authorized service object.

  Args:
    analytics: an authorized service object.
  Returns:
    An authorized service object with a lovely gav4 applied.
  """
  analytics.gav4_get = partial(gav4_get, analytics)


def convert_column_headers(report):
  """Converts the V4 report headers into the V3 report column headers.

  Args:
    report: a Google Analytics V4 Report object.
  Returns:
    A list of V3 report column headers.
  """
  column_header = report.get('columnHeader', {})
  dimensions = column_header.get('dimensions', [])
  metric_headers = column_header.get('metricHeader').get('metricHeaderEntries')

  headers = []
  for dimension in dimensions:
    if dimension == GA_SEGMENT:
      continue
    header = {}
    header['columnType'] = 'DIMENSION'
    header['dataType'] = 'STRING'
    header['name'] = dimension
    headers.append(header)
  for metric_header in metric_headers:
    header = {}
    header['columnType'] = 'METRIC'
    header['dataType'] = metric_header.get('type', 'FLOAT')
    header['name'] = metric_header.get('name', '')
    headers.append(header)
  return headers


def convert_rows(report):
  """Converts the V4 report row data into V3 report row data.

  Args:
    report: a Google Analytics V4 Report object.
  Returns:
    A list of rows of the V3 report object.
  """
  dimensions = report.get('columnHeader', {}).get('dimensions', [])

  rows = []
  report_data = report.get('data', {})
  for row in report_data.get('rows', []):
    row_data = []

    # Append the dimensions.
    for dimension, value in zip(dimensions, row.get('dimensions', [])):
      if dimension == GA_SEGMENT:
        continue
      row_data.append(value)

    # Append the metrics.
    for value in row.get('metrics', [])[0].get('values', []):
      row_data.append(value)

    rows.append(row_data)
  return rows


def convert_totals(report):
  """Converts the V4 report totals into the V3 report totals.

  Args:
    report: a Google Analytics V4 Report object.
  Returns:
    A list of rows of the V3 report object.
  """
  report_totals = report.get('data').get('totals')[0].get('values', [])
  metric_headers = report.get('columnHeader', {}).get(
      'metricHeader').get('metricHeaderEntries')

  totals = {}
  for metric_header, value in zip(metric_headers, report_totals):
    totals[metric_header.get('name')] = value
  return totals


def convert_report(report):
  """Converts the v4 report response into a v3 report response."""
  data = {}
  data['kind'] = 'analytics#gaData'
  data['columnHeaders'] = convert_column_headers(report)
  data['rows'] = convert_rows(report)
  data['totalsForAllResults'] = convert_totals(report)

  # Calculated sampling.
  report_data = report.get('data', {})
  sample_sizes = report_data.get('samplesReadCounts', [])
  sample_spaces = report_data.get('samplingSpaceSizes', [])
  if sample_sizes and sample_spaces:
    data['sampleSize'] = sample_sizes[0]
    data['sampleSpace'] = sample_spaces[0]
    data['containsSampledData'] = True
  else:
    data['containsSampledData'] = False

  data['isDataGolden'] = report_data.get('isDataGolden')
  if 'filteredForPrivacyReasons' in report_data:
    data['filteredForPrivacyReasons'] = report_data.get(
        'filteredForPrivacyReasons')

  return data
