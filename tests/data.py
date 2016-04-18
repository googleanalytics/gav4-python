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

"""This file contains requests and response objects for testing purposes."""

V3_RESPONSE = {
    "columnHeaders": [
        {
            "columnType": "DIMENSION",
            "dataType": "STRING",
            "name": "ga:source"
        },
        {
            "columnType": "DIMENSION",
            "dataType": "STRING",
            "name": "ga:city"
        },
        {
            "columnType": "METRIC",
            "dataType": "INTEGER",
            "name": "ga:sessions"
        },
        {
            "columnType": "METRIC",
            "dataType": "INTEGER",
            "name": "ga:users"
        }
    ],
    "containsSampledData": False,
    "id": "https://www.googleapis.com/analytics/v3/data/ga?ids=ga:90851825&dimensions=ga:source,ga:city&metrics=ga:sessions,ga:users&sort=-ga:sessions,ga:source&filters=ga:source%3D%3Dgoogle&segment=sessions::condition::ga:city!~not&start-date=2014-11-01&end-date=2014-11-30&max-results=25",
    "itemsPerPage": 25,
    "kind": "analytics#gaData",
    "profileInfo": {
        "accountId": "54535478",
        "internalWebPropertyId": "87498559",
        "profileId": "90851825",
        "profileName": "All Web Site Data",
        "tableId": "ga:90851825",
        "webPropertyId": "UA-54535478-1"
    },
    "query": {
        "dimensions": "ga:source,ga:city",
        "end-date": "2014-11-30",
        "filters": "ga:source==google",
        "ids": "ga:90851825",
        "max-results": 25,
        "metrics": [
            "ga:sessions",
            "ga:users"
        ],
        "samplingLevel": "FASTER",
        "segment": "sessions::condition::ga:city!~not",
        "sort": [
            "-ga:sessions",
            "ga:source"
        ],
        "start-date": "2014-11-01",
        "start-index": 1
    },
    "rows": [
        [
            "google",
            "Philadelphia",
            "60",
            "5"
        ],
        [
            "google",
            "Johnstown",
            "21",
            "1"
        ],
        [
            "google",
            "Progress",
            "7",
            "1"
        ],
        [
            "google",
            "Scranton",
            "2",
            "1"
        ],
        [
            "google",
            "Burgess Hill",
            "1",
            "1"
        ],
        [
            "google",
            "Los Angeles",
            "1",
            "1"
        ],
        [
            "google",
            "San Francisco",
            "1",
            "1"
        ],
        [
            "google",
            "Santa Clara",
            "1",
            "1"
        ]
    ],
    "selfLink": "https://www.googleapis.com/analytics/v3/data/ga?ids=ga:90851825&dimensions=ga:source,ga:city&metrics=ga:sessions,ga:users&sort=-ga:sessions,ga:source&filters=ga:source%3D%3Dgoogle&segment=sessions::condition::ga:city!~not&start-date=2014-11-01&end-date=2014-11-30&max-results=25",
    "totalResults": 8,
    "totalsForAllResults": {
        "ga:sessions": "94",
        "ga:users": "12"
    }
}


V4_RESPONSE = {
    "reports": [
        {
            "columnHeader": {
                "dimensions": [
                    "ga:source",
                    "ga:city",
                    "ga:segment"
                ],
                "metricHeader": {
                    "metricHeaderEntries": [
                        {
                            "name": "ga:sessions",
                            "type": "INTEGER"
                        },
                        {
                            "name": "ga:users",
                            "type": "INTEGER"
                        }
                    ]
                }
            },
            "data": {
                "isDataGolden": True,
                "maximums": [
                    {
                        "values": [
                            "60",
                            "5"
                        ]
                    }
                ],
                "minimums": [
                    {
                        "values": [
                            "1",
                            "1"
                        ]
                    }
                ],
                "rowCount": 8,
                "rows": [
                    {
                        "dimensions": [
                            "google",
                            "Philadelphia",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "60",
                                    "5"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "Johnstown",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "21",
                                    "1"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "Progress",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "7",
                                    "1"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "Scranton",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "2",
                                    "1"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "Burgess Hill",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "1",
                                    "1"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "Los Angeles",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "1",
                                    "1"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "San Francisco",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "1",
                                    "1"
                                ]
                            }
                        ]
                    },
                    {
                        "dimensions": [
                            "google",
                            "Santa Clara",
                            "Dynamic Segment"
                        ],
                        "metrics": [
                            {
                                "values": [
                                    "1",
                                    "1"
                                ]
                            }
                        ]
                    }
                ],
                "totals": [
                    {
                        "values": [
                            "94",
                            "12"
                        ]
                    }
                ]
            }
        }
    ]
}

V4_REQUEST = {
    "reportRequests": [
        {
            "dateRanges": [
                {
                    "endDate": "2014-11-30",
                    "startDate": "2014-11-01"
                }
            ],
            "dimensions": [
                {
                    "name": "ga:source"
                },
                {
                    "name": "ga:city"
                },
                {
                    "name": "ga:segment"
                }
            ],
            "filtersExpression": "ga:source==google",
            "metrics": [
                {
                    "expression": "ga:sessions"
                },
                {
                    "expression": "ga:users"
                }
            ],
            "order_bys": [
                {
                    "fieldName": "ga:sessions",
                    "sortOrder": "DESCENDING",
                    "orderType": "VALUE"
                },
                {
                    "fieldName": "ga:source",
                    "orderType": "VALUE"
                }
            ],
            "pageSize": "25",
            "samplingLevel": "SMALL",
            "segments": [
                {
                    "segmentId": "sessions::condition::ga:city!~not"
                }
            ],
            "viewId": "ga:90851825"
        }
    ]
}


V3_CONVERTED_RESPONSE = {
    "columnHeaders": [
        {
            "columnType": "DIMENSION",
            "dataType": "STRING",
            "name": "ga:source"
        },
        {
            "columnType": "DIMENSION",
            "dataType": "STRING",
            "name": "ga:city"
        },
        {
            "columnType": "METRIC",
            "dataType": "INTEGER",
            "name": "ga:sessions"
        },
        {
            "columnType": "METRIC",
            "dataType": "INTEGER",
            "name": "ga:users"
        }
    ],
    "containsSampledData": False,
    "isDataGolden": True,
    "kind": "analytics#gaData",
    "rows": [
        [
            "google",
            "Philadelphia",
            "60",
            "5"
        ],
        [
            "google",
            "Johnstown",
            "21",
            "1"
        ],
        [
            "google",
            "Progress",
            "7",
            "1"
        ],
        [
            "google",
            "Scranton",
            "2",
            "1"
        ],
        [
            "google",
            "Burgess Hill",
            "1",
            "1"
        ],
        [
            "google",
            "Los Angeles",
            "1",
            "1"
        ],
        [
            "google",
            "San Francisco",
            "1",
            "1"
        ],
        [
            "google",
            "Santa Clara",
            "1",
            "1"
        ]
    ],
    "totalsForAllResults": {
        "ga:sessions": "94",
        "ga:users": "12"
    }
}


ORDER_BYS = [
    {
        "fieldName": "ga:country",
        "orderType": "VALUE"
    },
    {
        "fieldName": "ga:browser",
        "sortOrder": "DESCENDING",
        "orderType": "VALUE"
    },
    {
        "fieldName": "ga:sessions",
        "sortOrder": "DESCENDING",
        "orderType": "VALUE"
    }
]

V3_REQUEST = {
    "ids": "ga:90851825",
    "start_date": "2014-11-01",
    "end_date": "2014-11-30",
    "metrics": "ga:sessions,ga:users",
    "dimensions": "ga:source,ga:city",
    "segment": "sessions::condition::ga:city!~not",
    "sort": "-ga:sessions,ga:source",
    "filters": "ga:source==google",
    "max_results": "25",
    "samplingLevel": "FASTER",
}


class BatchGet(object):
  """Mock class of the BatchGet Reports Request object."""

  def __init__(self, body):
    self.body = body

  def execute(self):
    """Mock of the Batch get execute method.

    Returns:
       A v4 response object.
    """
    return V4_RESPONSE


class Reports(object):
  """Mock class of the Google Analytics Reports object."""

  def batchGet(self, body):  # pylint: disable=invalid-name
    """Returns a mock BatchGet Object."""
    return BatchGet(body)


class AnalyticsReporting(object):
  """Mock AnalyticsReporting service object."""

  def reports(self):
    """Returns a mock Reports object."""
    return Reports()
