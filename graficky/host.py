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

class Host(object):
    """Defines a Graphite host."""
    def __init__(self, host='localhost', port=8080, username=None,
                 password=None, default_tz=None):
        self.host = host
        self.port = port

        # Attach basic auth headers to host if needed.
        if username and password:
            self.username = username
            self.password = password

        # TODO Sane default for default_tz
        self.default_tz = default_tz

    # TODO You may want to just make this an implementation of an abstract
    # method in Graficky that calls this by default, or calls this on multiple
    # Hosts in the Graficky instance and formats it to allow abstraction of
    # parallel behavior from this implementation.
    def get_metric(self, metric, format=None):
        """Returns a list of (datetime, data) tuples for the given key. The key
        string must match only one key or an exception will be thrown. Optional
        format parameter will return Graphite string output for the Graphite
        format specified.

        :param metric: the metric key, for example "my.really.long.metric.name"
        TODO If we have a Metric object, what will it include?
        :param format: if specified, return Graphite data as a string for this
        format.  Options are raw, csv, and json. See Graphite documentation for
        what is returned with these optoins.

        :returns: list of (datetime, data) tuples
        TODO Or, return a Metric object once the interfaces are more fleshed
        out
        """
        pass

    def list_all_metrics(self):
        """ :returns: a list of strings specifying all metric keys available on
        the Host """
        pass

    def list_empty_metrics(self, time_span_from, time_span_until=None,
                           delete=False):
        """Lists the metrics for which there's no data in the given timespan.

        :param delete: whether to delete these metrics from Graphite. Use with
        caution.

        TODO You may not be able to do this through the Graphite API. In the
        future, support something that can actually get onto the server /
        db and delete things.
        """
        pass

    def list_under(self, base=None, depth=1, only_keys=False, only_dirs=False):
        """Lists metric titles under this base directory or metric name, to
        this depth. Items in the list are tuples of (name, is_key), where
        is_key is True if this name is an actual metric key, False if this is a
        "directory" with other "directories" or metric keys under it.

        TODO Make examples using the depth parameter and document what it does..

        Example:

        You have a Graphite server with the following metrics.

        graficky
            icky_metrics
                gross (full key is graficky.icky_metrics.gross)
                silly (graficky.icky_metrics.silly)
            graficky_users (full key is graficky.icky_users)

        List the top level of the tree:

        > host.list_under()
        [('graficky', False)]

        > host.list_under('graficky')
        [('graficky.icky_metrics', False), ('graficky.graficky_users', True)]]

        > host.list_under('graficky.icky_metrics')
        [('graficky.icky_metrics.gross', True),
         ('graficky.icky_metrics', True)]
        """
        pass
