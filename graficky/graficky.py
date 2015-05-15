# -*- encoding: utf-8 -*-
#
# Copyright 2015 Mario Villaplana
#
# Author: Mario Villaplana <mario.villaplana@rackspace.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import requests

class Graficky(object):

    def __init__(self):
        # TODO
        self.hosts = []
        self.default_host = ''
        self.parallel = False
        self.timeout = -1 # TODO Allow specifying timeout on per-host basis?

'''
 Things this should support:
 - Python 2.7 and 3!
 - Working with multiple Graphite Hosts simultaneously
    - Maybe have a Graficky have 1 host for the default, and support multiple
      hosts. Graficky has parallel option that is False by default, throws
      error if you don't have a default host set, have more than 1 host, and
      haven't enabled parallel operations.
    - Support performing same operation - every operation that you can do on
      one host, you should be able to do on multiple hosts in parallel with
      parallel option.
 - Listing metric names available under a Host. Use wildcards or a more
   efficient strategy to implement - see if there's a way to spec number of
   metrics to receive as 0. Support several options - from this start point,
   list metrics or metric directories N levels under me (1 by default).  List
   all metrics names.
    - If operating on multiple hosts in parallel mode, specify the behavior.
      Default, perhaps label metric names by host individually. Allow retrieval
      of common metrics separately from metrics on an individual host, e.g.
      { 'common': [ ... list of metric keys ...],
        'host_1': [ ... metric keys in host_1, not in host_2 ...],
        'host_2': [ ... metric keys in host_2, not in host_1 ...]
      }
 - Utilities:
    - Convert all Graphite date strings to datetime objects by default, and
      accept datetime objects by default. Make it easy to work with datetime
      objects, Unix epoch times, and maybe Graphite date strings.
      - Have separate functions if you just want to use this part of the lib
 - Performing common operations on metrics
    - Count the number of datapoints in this metric
    - Return metrics as:
        - Graphite defaults
            - json, csv, raw
        - Python list of just values
        - Python list of tuples (datetime, value)
    - Support for renaming metrics
    - Support for merging two metrics into 1 with merge options
    - Find metrics with no data for the past N days, with delete option for
      this
    - Support all Graphite built-in functions with a better interface
 - Make useful errors like MetricNotFound, HostNotFound, HostTimeout with a
   sane default
 - Future: support for generating URLs for visual graphs? support for saving
   metrics to disk with something like pickle? some useful things for
   instrumenting performance and sending to Graphite? < might already exist
 - Rackspace Cloud Metrics integration? Other Graphite as a service
   integrations?
'''
