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

from datetime import datetime, timedelta

# TODO Rename all these functions.
def convert_graphite_to_datetime(time):
    # TODO Make this work with more than just the below times.
    # Add support for specifying timezone.
    # Add special error type if conversion failed
    # Fix docstring.
    """Converts a Graphite time string to datetime object."""
    if time is None:
        return None
    elif time == '-1hours':
        return datetime.now() - timedelta(hours=1)
    elif time == '-24hours':
        return datetime.now() - timedelta(hours=24)
    elif time == '-7days':
        return datetime.now() - timedelta(days=7)
    elif time == '-30days':
        return datetime.now() - timedelta(days=30)
    else:
        return datetime.strptime(time, '%H:%M_%Y%m%d')

def is_graphite_datetime(time):
    # TODO Fix this to work with refactoring of above fn
    """Returns true if time string is a valid Graphite date string, false
    otherwise."""
    try:
        time = convert_graphite_to_datetime(time)
        if time is not None:
            # If conversion to datetime succeeds, return true
            return True
        else:
            return False
    except ValueError as e:
        # Conversion to datetime failed
        return False

# TODO Make this work with object-oriented interface, do error checking, maybe
# move it to a different file.
def get_graphite_count(graphite_json, pprint=False):
    """Retrieves the length of the list of datapoints that are not None from a
    JSON response from Graphite."""
    count = 0
    if type(graphite_json) == type([]) and len(graphite_json) > 0:
        for datapoint in graphite_json[0]['datapoints']:
            if datapoint[0] is not None:
                count += 1
    return count
