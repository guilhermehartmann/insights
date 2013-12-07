#
# Copyright 2013 Quantopian, Inc.
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


import logbook
from intuition.zipline.data_source import DataFactory
from intuition.data.quandl import DataQuandl


log = logbook.Logger('intuition.source.backtest.quandl')


class QuandlSource(DataFactory):
    """
    Fetchs data from quandl.com
    """

    def get_data(self):
        #TODO Works here for one value, make it later a panel

        # API key must be provided here or store in the environment
        # (QUANDL_API_KEY)
        feed = DataQuandl()
        assert len(self.sids) == 1

        return feed.fetch(self.sids[0],
                          start_date=self.start,
                          end_date=self.end,
                          returns='pandas')

    @property
    def mapping(self):
        return {
            'dt': (lambda x: x, 'dt'),
            'sid': (lambda x: x, 'sid'),
            'price': (float, 'Close'),
            'volume': (int, 'Volume'),
            'open': (int, 'Open'),
            'low': (int, 'Low'),
            'high': (int, 'High'),
        }
